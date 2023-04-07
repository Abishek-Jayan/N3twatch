let download_list = {};

browser.downloads.onCreated.addListener((e) => {
    download_list[e.id] = e.filename;
});
browser.downloads.onChanged.addListener((e) => {
    if (e.state.current === "complete") {
        if (download_list[e.id]) {

            let request = new Request("http://localhost:8080/dwnld_state", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                        "path": download_list[e.id],
                        "download_state": e.state.current,
                        "download_id": e.id,
                    }),

          });
          fetch(request).catch((error) => {
            console.error(error);
            });

            delete download_list[e.id];
        }
    }
});
