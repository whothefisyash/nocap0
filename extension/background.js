chrome.runtime.onInstalled.addListener(() => {
    chrome.contextMenus.create({
        id: "factCheck",
        title: "Check Misinformation with NoCap",
        contexts: ["selection"]
    });
});

chrome.contextMenus.onClicked.addListener((info, tab) => {
    if (info.menuItemId === "factCheck") {
        chrome.storage.local.set({ selectedText: info.selectionText }, () => {
            chrome.action.openPopup();
        });
    }
});
