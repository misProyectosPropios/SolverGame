let pyodide;
let python_code;
let isSolving = false;
let solverReady = false;

function setStatus(message) {
    document.getElementById("status").textContent = message;
}

async function init() {
    if (window.location.protocol === "file:") {
        throw new Error("Open this app from http://localhost:8000 instead of opening index.html directly.");
    }

    pyodide = await loadPyodide();

    const response = await fetch("decider.py");
    if (!response.ok) {
        throw new Error(`Could not load decider.py: ${response.status} ${response.statusText}`);
    }

    python_code = await response.text();
    pyodide.FS.writeFile("decider.py", python_code);

    await pyodide.runPythonAsync(`
import sys
if "" not in sys.path:
    sys.path.append("")
    `);

    document.getElementById("solveBtn").disabled = false;
    solverReady = true;
    setStatus("Solver ready.");
    return pyodide;
}

let pyodideReadyPromise = init();
pyodideReadyPromise.catch((error) => {
    setStatus(error.message);
});

async function run() {
    if (isSolving) {
        return;
    }

    isSolving = true;
    document.getElementById("solveBtn").disabled = true;
    setStatus("Solving...");

    try {
        let pyodide = await pyodideReadyPromise;

        const numbers = [
            document.getElementById("number1").value,
            document.getElementById("number2").value,
            document.getElementById("number3").value,
            document.getElementById("number4").value,
        ];
        const target = document.getElementById("target").value;

        const result = await pyodide.runPythonAsync(`
import sys
if "decider" in sys.modules:
    del sys.modules["decider"]

import decider

nums = [decider.Constant(int(x)) for x in ${JSON.stringify(numbers)}]
res = decider.obtainSolution(nums, int(${JSON.stringify(target)}))

[f"{str(r)} = {r.evaluateAST()}" for r in res[:20]]
`);

        const resultList = document.getElementById("result-list");
        resultList.innerHTML = "";

        result.toJs().forEach((solution) => {
            const item = document.createElement("li");
            item.textContent = solution;
            resultList.appendChild(item);
        });
        setStatus("Solver ready.");
    } catch (error) {
        setStatus(error.message);
    } finally {
        isSolving = false;
        document.getElementById("solveBtn").disabled = !solverReady;
    }
}

document.getElementById("solver-form").addEventListener("submit", (event) => {
    event.preventDefault();
    run();
});
