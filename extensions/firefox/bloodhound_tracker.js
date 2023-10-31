API_KEY = "hb2tx1w4131aad44gz56y9d019462476wuatj4ra389c25897bqgmr085d489ab1";
API_SUMMARY_URL = "https://www.hybrid-analysis.com/api/v2/overview/";
API_UPLOAD_URL = "https://www.hybrid-analysis.com/api/v2/quick-scan/url";

browser.downloads.onCreated.addListener(async (e) => {
  //Pause the download here
  console.log(e);
  browser.downloads.pause(e.id);
  console.log("Paused");
  const headers = {
    "api-key": API_KEY,
    "Content-Type": "application/json",
  };
  const data = {
    scan_type: "all",
    url: e.url.trim(),
  };

  // Perform the POST request using the Fetch API
  try {
    const response = await fetch(API_UPLOAD_URL, {
      method: "POST",
      headers: headers,
      body: JSON.stringify(data),
    });
    if (response.ok) {
      const responseData = await response.json();
      const sha = responseData.sha256;

      // Make a GET request to retrieve the summary
      const summaryResponse = await fetch(`${API_SUMMARY_URL}${sha}/summary`, {
        headers: headers,
      });

      if (summaryResponse.ok) {
        const summaryData = await summaryResponse.json();
        if (summaryData.threat_score) {
          console.log("Kill it with Fire!!!");
          browser.downloads.cancel(e.id);
        } else {
          console.log("All clear");
          browser.downloads.resume(e.id);
        }
      } else {
        console.log(
          "Failed to fetch summary:",
          summaryResponse.status,
          summaryResponse.statusText
        );
      }
    } else {
      console.log(
        "Failed to upload the URL:",
        response.status,
        response.statusText
      );
    }
  } catch (error) {
    console.error("An error occurred:", error);
  }
});
