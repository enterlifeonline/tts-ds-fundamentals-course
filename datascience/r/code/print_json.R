library(RJSONIO)
# from the website
foodMarketsRaw <- fromJSON("https://data.ny.gov/api/views/9a8c-vfzj/rows.json?accessType=DOWNLOAD")

# if you download
# foodMarketRaw <- fromJSON("retail_food_markets.json")

#extract the data
foodMarkets <- foodMarketsRaw[['data']]

# name the food market 1
foodMarkets[[1]][[14]]

# name of food market 2
foodMarkets[[2]][[14]]

fmNames <- sapply(foodMarkets, function(x) x[[14]])
head(fmNames)

# for the trim function
library(gdata)
grabInfo <- function(var){
  print(paste("Variable", var, sep=" "))
  sapply(foodMarkets, function(x) returnData(x, var))
}

returnData <- function(x, var){
  if(!is.null( x[[var]])){
  	return( trim(x[[var]]))
  	}else{
  		return(NA)
  	}
}

# do the extraction and assembly
 fmDataDF <- data.frame(sapply(1:22, grabInfo), stringsAsFactors=FALSE)

#print 
fmDataDF

# extracting geography
foodMarkets[[1]][[23]]

grabGeoInfo<-function(val){

    l<- length(foodMarkets[[1]][[val]])
    tmp<-lapply(1:l, function(y) 

      sapply(foodMarkets, function(x){

        if(!is.null(x[[val]][[y]])){
          return(x[[val]][[y]])
        }else{
          return(NA)
        }

        })     
      )
}

# add the names

columns<-foodMarketsRaw[['meta']][['view']][['columns']]

#extract names for geo or non-geo

getNames<-function(x){
  if(is.null(columns[[x]]$subColumnTypes)){
    return(columns[[x]]$name)
  }else{
    return(columns[[x]]$subColumnTypes)
  }
}

fmNames<-unlist(sapply(1:length(columns), getNames))

# add names to dataset

names(fmDataDF)<-fmNames
head(fmDataDF)

# long lat
fmDataDF$latitude<-as.numeric(fmDataDF$latitude)
fmDataDF$longitude<-as.numeric(fmDataDF$longitude)

#visualization
library(rgdal)
library(ggplot2)
state<-readOGR("X:/administrative/social_media/blogposts/json_from_R", layer="nys")
## OGR data source with driver: ESRI Shapefile 
## Source: "X:/administrative/social_media/blogposts/json_from_R", layer: "nys"
## with 1 features and 53 fields
## Feature type: wkbMultiPolygon with 2 dimensions