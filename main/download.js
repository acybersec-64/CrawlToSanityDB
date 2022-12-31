


fs = require('fs');
'use strict';

const args = require('minimist')(process.argv.slice(2));
console.log("downloading "+args._[0]);


// -------------------------- downloading each code page ---------------------------------------
let fetcToAnzcoPageByCode = fetch(`https://www.anzscosearch.com/${args._[0]}/`, {
    "headers": {
      "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
      "accept-language": "en-US,en;q=0.9,fa;q=0.8",
      "cache-control": "max-age=0",
      "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Microsoft Edge\";v=\"108\"",
      "sec-ch-ua-mobile": "?0",
      "sec-ch-ua-platform": "\"Windows\"",
      "sec-fetch-dest": "document",
      "sec-fetch-mode": "navigate",
      "sec-fetch-site": "same-origin",
      "sec-fetch-user": "?1",
      "upgrade-insecure-requests": "1",
      "cookie": `"${args._[1]}"`,
      "Referer": "https://www.anzscosearch.com/search/",
      "Referrer-Policy": "strict-origin-when-cross-origin"
    },
    "body": null,
    "method": "GET"
  }).then(res => res.text()).then((data) => {
    // ---------------------   saving them ---------------------------------
    fs.writeFile(`../all_pages/${args._[0]}.html`, `${data}`, function (err) {
    if (err) return console.log(err);
    console.log("done");
    });
    return data;
}); 

