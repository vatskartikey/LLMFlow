document.getElementById("uploadForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const file = document.getElementById("fileInput").files[0];
  const formData = new FormData();
  formData.append("file", file);

  const outputDiv = document.getElementById("output");
  outputDiv.innerHTML = "<p>Processing...</p>";

  const response = await fetch("http://127.0.0.1:5000/upload", {
    method: "POST",
    body: formData
  });

  const result = await response.json();
  outputDiv.innerHTML = `<pre>${result.response}</pre>`;
});
