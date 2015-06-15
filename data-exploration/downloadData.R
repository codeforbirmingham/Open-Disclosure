#####################################################################
# Use this script to download the latest aggregated Alabama campaign
# finance transaction data from Code for Birmingham's Socrata open 
# data portal!
# 
# Our data portal may be found here:
# https://brigades.opendatanetwork.com/catalog?Brigade_Group=Code%20for%20Birmingham
#
# How to use this script:
# 1. Source the script into your R environment
# 2. Run clearData() to get rid of old data
# 3. Get the latest data from our Socrata data portal using downloadData()
#
# Last revised: 15 June 2015
# Contributor(s): Tarif Haque
#####################################################################

# Warning! Deletes all data from the data directory.
clearData <- function() {
  do.call(file.remove, list(list.files("data/", full.names=TRUE)))
}

# Download the latest Alabama campaign finance data from Socrata!
downloadData <- function() {
  
  # create data directory if it does not exist
  if(!file.exists("data")) {
    dir.create("data")
  }
  
  dateDownloaded <- date()
  
  # download the latest transactions data if it does not exist
  if (!file.exists("data/transactions.csv")) {
    fileURL <- "https://brigades.opendatanetwork.com/api/views/vcap-yyfq/rows.csv?accessType=DOWNLOAD"
    download.file(fileURL, destfile = './data/transactions.csv', method = 'curl')
    
    # load the data
    transactions <- read.csv("./data/transactions.csv", header = TRUE)
  }
  
  # download the latest parties data if it does not exist
  if (!file.exists("data/parties.csv")) {
    fileURL <- "https://brigades.opendatanetwork.com/api/views/ucem-puhh/rows.csv?accessType=DOWNLOAD"
    download.file(fileURL, destfile = './data/parties.csv', method = 'curl')
    
    # load the data
    parties <- read.csv("./data/parties.csv", header = TRUE)
  }
  
  # download the latest districts data if it does not exist
  if (!file.exists("data/districts.csv")) {
    fileURL <- "https://brigades.opendatanetwork.com/api/views/p8kt-epji/rows.csv?accessType=DOWNLOAD"
    download.file(fileURL, destfile = './data/districts.csv', method = 'curl')
    
    # load the data
    districts <- read.csv("./data/districts.csv", header = TRUE)
  }
  
  # download the latest transactees data if it does not exist
  if (!file.exists("data/transactees.csv")) {
    fileURL <- "https://brigades.opendatanetwork.com/api/views/9xmj-xdkh/rows.csv?accessType=DOWNLOAD"
    download.file(fileURL, destfile = './data/transactees.csv', method = 'curl')
    
    # load the data
    transactees <- read.csv("./data/transactees.csv", header = TRUE)
  }
  
  list(date = dateDownloaded, transactions = transactions, parties = parties, 
       districts = districts, transactees = transactees)
}