// static/app.js

document.addEventListener("DOMContentLoaded", () => {
    // Handle Create Rule form submission
    const createRuleForm = document.getElementById("createRuleForm");
    createRuleForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        const ruleName = document.getElementById("ruleName").value;
        const ruleString = document.getElementById("ruleString").value;

        try {
            const response = await fetch('/create_rule', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ rule_name: ruleName, rule_string: ruleString }),
            });

            const result = await response.json();
            if (response.ok) {
                document.getElementById("createRuleResult").textContent = "Rule created successfully!";
            } else {
                document.getElementById("createRuleResult").textContent = `Error: ${result.error}`;
            }
        } catch (error) {
            document.getElementById("createRuleResult").textContent = `Network error: ${error.message}`;
        }
    });

    // Handle Evaluate Rule form submission
    const evaluateRuleForm = document.getElementById("evaluateRuleForm");
    evaluateRuleForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        const ruleData = document.getElementById("ruleData").value;

        try {
            const response = await fetch('/evaluate_rule', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ rule_data: JSON.parse(ruleData) }),
            });

            const result = await response.json();
            if (response.ok) {
                document.getElementById("evaluateRuleResult").textContent = `Evaluation Result: ${result.result}`;
            } else {
                document.getElementById("evaluateRuleResult").textContent = `Error: ${result.error}`;
            }
        } catch (error) {
            document.getElementById("evaluateRuleResult").textContent = `Network error: ${error.message}`;
        }
    });
});
