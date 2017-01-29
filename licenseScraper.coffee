# Script I made to scrape all open source licenses and save them to named .txt
# files locally.

fs = require('fs')
request = require('request')
request = request.defaults({jar: true})
cheerio = require('cheerio')
Regex = require('regex')

regex = new Regex(/(\/licenses\/)([a-zA-Z0-9]*)/)

baseUrl = "https://opensource.org"
licensesUrl = "/licenses/category"

request(baseUrl + licensesUrl, (err, message, body)->
  $ = cheerio.load(body)
  index = 0
  urls = []
  for obj in $('li').find('a')
    if obj.attribs['href'].indexOf('/licenses/') != -1
      index++
      if index > 2
        urls.push(obj.attribs['href'])

  urls.forEach((url, index)->
    request(baseUrl + url, (err, message, body)->
      $ = cheerio.load(body)
      licenseHtml = $('#page').html()
      $ = cheerio.load(licenseHtml)

      urlWords = url.split('/')
      docName = urlWords[2]

      fs.writeFile('licenses/' + docName + '.html', licenseHtml, (err)->
        if err?
          console.log err
      )
    )
  )
)