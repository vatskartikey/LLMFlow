import puter from "puter-js";

const args = process.argv.slice(2);
const inputText = args.join(" ");
const prompt = `Analyze this documentation and classify errors into:
1. Source
2. Sink
3. Sanitizer
Also describe potential issues.\n\nDocument:\n${inputText}`;

const response = await puter.ai.chat(prompt, { model: "gpt-5-nano" });
console.log(response.output_text);
