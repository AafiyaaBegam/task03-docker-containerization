
const statusElement = document.querySelector("#status");
const detailsElement = document.querySelector("#details");
const refreshButton = document.querySelector("#refresh");

async function checkService() {
  statusElement.textContent = "Checking service...";
  statusElement.dataset.state = "loading";
  detailsElement.textContent = "Connecting to /health...";

  try {
    const response = await fetch("/health");
    const result = await response.json();

    detailsElement.textContent = JSON.stringify(result, null, 2);

    if (response.ok && result.status === "healthy") {
      statusElement.textContent = "All services healthy";
      statusElement.dataset.state = "healthy";
    } else {
      statusElement.textContent = "Service degraded";
      statusElement.dataset.state = "degraded";
    }
  } catch (error) {
    statusElement.textContent = "Service unavailable";
    statusElement.dataset.state = "error";
    detailsElement.textContent =
      "Unable to reach the API. Check the application and try again.";
  }
}

refreshButton.addEventListener("click", checkService);
checkService();
