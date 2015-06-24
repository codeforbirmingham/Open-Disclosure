#####################################################################
# Use this script to get the latest aggregated Alabama campaign
# finance transaction data from Code for Birmingham's Socrata open 
# data portal, and load it into your R environment!
# 
# Our data portal may be found here:
# https://brigades.opendatanetwork.com/catalog?Brigade_Group=Code%20for%20Birmingham
#
# Last revised: 15 June 2015
# Contributor(s): Tarif Haque
#####################################################################

# Warning! Deletes all data from the "data-exploration/data" directory.
clearData <- function() {
  do.call(file.remove, list(list.files("data/", full.names=TRUE)))
}

# Checks if all data files already exist.
allDataExists <- function() {
  file.exists("data/transactions.csv") & file.exists("data/transactees.csv") &
    file.exists("data/parties.csv") & file.exists("data/districts.csv")
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
  }
  
  # download the latest parties data if it does not exist
  if (!file.exists("data/parties.csv")) {
    fileURL <- "https://brigades.opendatanetwork.com/api/views/ucem-puhh/rows.csv?accessType=DOWNLOAD"
    download.file(fileURL, destfile = './data/parties.csv', method = 'curl')
  }
  
  # download the latest districts data if it does not exist
  if (!file.exists("data/districts.csv")) {
    fileURL <- "https://brigades.opendatanetwork.com/api/views/p8kt-epji/rows.csv?accessType=DOWNLOAD"
    download.file(fileURL, destfile = './data/districts.csv', method = 'curl')
  }
  
  # download the latest transactees data if it does not exist
  if (!file.exists("data/transactees.csv")) {
    fileURL <- "https://brigades.opendatanetwork.com/api/views/9xmj-xdkh/rows.csv?accessType=DOWNLOAD"
    download.file(fileURL, destfile = './data/transactees.csv', method = 'curl')
  }
  
  # return a list with all the downloaded data
  list(date = dateDownloaded, transactions = transactions, parties = parties, 
       districts = districts, transactees = transactees)
}

# Assumes data has already been downloaded into "data/data-exploration" directory.
# Loads all the data into our R environment.
loadData <- function() {
  transactions <- read.csv("./data/transactions.csv", header = TRUE)
  transactees <- read.csv("./data/transactees.csv", header = TRUE)
  parties <- read.csv("./data/parties.csv", header = TRUE)
  districts <- read.csv("./data/districts.csv", header = TRUE)
}

# Download data if all data does not exist
if (!allDataExists()) {
  downloadData();
} 

loadData();