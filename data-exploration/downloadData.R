downloadData <- function() {
  
  # create data directory if it does not exist
  if(!file.exists("data")) {
    dir.create("data")
  }
  
  # download the latest transactions data if it does not exist
  if (!file.exists("data/transactions.csv")) {
    fileURL <- "https://brigades.opendatanetwork.com/api/views/vcap-yyfq/rows.csv?accessType=DOWNLOAD"
    download.file(fileURL, destfile = './data/transactions.csv', method = 'curl')
    dateDownloaded <- date()
  }
  
  # load the data
  transactions <- read.csv("./data/transactions.csv", header = TRUE)
  
  data.frame(transactions)
}