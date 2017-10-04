
## Write a function called best that take two arguments: the 2-character abbreviated name of a state and an
## outcome name. The function reads the outcome-of-care-measures.csv le and returns a character vector
## with the name of the hospital that has the best (i.e. lowest) 30-day mortality for the specied outcome
## in that state.
best <- function(state, outcome) {
    ## Read outcome data
    outcomeall <- read.csv("B:\\OneDrive\\Documents\\coursera\\R programming\\rprog-data-ProgAssignment3-data\\outcome-of-care-measures.csv", colClasses = "character")
    
    
    ## Check that state and outcome are valid
    statecheck=state %in% unique(outcomeall$State)
    if (!statecheck){
        stop("invalid state")
    }
    outcomecheck=outcome %in% c("heart attack", "heart failure", "pneumonia")
    if (!outcomecheck){
        stop("invalid outcome")
    }    
    
    
    ##get the state data and corresponding response column
    statedata=subset(outcomeall,State==state)
    if(outcome=="heart attack"){
        statedata=subset(statedata, select=c(Hospital.Name,Hospital.30.Day.Death..Mortality..Rates.from.Heart.Attack))
    } else if(outcome=="heart failure"){
        statedata=subset(statedata, select=c(Hospital.Name,Hospital.30.Day.Death..Mortality..Rates.from.Heart.Failure))
        
    }else{
        statedata=subset(statedata, select=c(Hospital.Name,Hospital.30.Day.Death..Mortality..Rates.from.Pneumonia))
    }
    
    
    ## Return hospital name in that state with lowest 30-day death
    ## get the statistics for each hospital
    stat=tapply(as.numeric(statedata[,2]),as.factor(statedata[,1]),mean)
    stat <- stat[!is.na(stat)]
    stat=sort(stat)
    names(stat[1])
}

## Write a function called rankhospital that takes three arguments: the 2-character abbreviated name of a
## state (state), an outcome (outcome), and the ranking of a hospital in that state for that outcome (num).
## The function reads the outcome-of-care-measures.csv le and returns a character vector with the name
## of the hospital that has the ranking specied by the num argument


rankhospital <- function(state, outcome,num="best") {
    ## Read outcome data
    outcomeall <- read.csv("B:\\OneDrive\\Documents\\coursera\\R programming\\rprog-data-ProgAssignment3-data\\outcome-of-care-measures.csv", colClasses = "character")
    
    
    ## Check that state and outcome are valid
    statecheck=state %in% unique(outcomeall$State)
    if (!statecheck){
        stop("invalid state")
    }
    outcomecheck=outcome %in% c("heart attack", "heart failure", "pneumonia")
    if (!outcomecheck){
        stop("invalid outcome")
    }    
    
    
    ##get the state data and corresponding response column
    statedata=subset(outcomeall,State==state)
    if(outcome=="heart attack"){
        statedata=subset(statedata, select=c(Hospital.Name,Hospital.30.Day.Death..Mortality..Rates.from.Heart.Attack))
    } else if(outcome=="heart failure"){
        statedata=subset(statedata, select=c(Hospital.Name,Hospital.30.Day.Death..Mortality..Rates.from.Heart.Failure))
        
    }else{
        statedata=subset(statedata, select=c(Hospital.Name,Hospital.30.Day.Death..Mortality..Rates.from.Pneumonia))
    }
    
    
    ## Return hospital name in that state with lowest 30-day death
    ## get the statistics for each hospital
    stat=tapply(as.numeric(statedata[,2]),as.factor(statedata[,1]),mean)
    stat <- stat[!is.na(stat)]
    stat=sort(stat)
    if(num=="best"){num=1}
    else if(num=="worst"){num=length(stat)}
    
    names(stat[num])
}



## Write a function called rankall that takes two arguments: an outcome name (outcome) and a hospital rank-
## ing (num). The function reads the outcome-of-care-measures.csv le and returns a 2-column data frame
## containing the hospital in each state that has the ranking specied in num. For example the function call
## rankall("heart attack", "best") would return a data frame containing the names of the hospitals that
## are the best in their respective states for 30-day heart attack death rates.

rankall <- function(outcome,num="best") {
    ## Read outcome data
    outcomeall <- read.csv("B:\\OneDrive\\Documents\\coursera\\R programming\\rprog-data-ProgAssignment3-data\\outcome-of-care-measures.csv", colClasses = "character")
    
    
    ## Check that outcome are valid
    outcomecheck=outcome %in% c("heart attack", "heart failure", "pneumonia")
    if (!outcomecheck){
        stop("invalid outcome")
    }    
    
    
    ##get the corresponding response column for each state
    if(outcome=="heart attack"){
        subdata=subset(outcomeall, select=c(State,Hospital.Name,Hospital.30.Day.Death..Mortality..Rates.from.Heart.Attack))
    } else if(outcome=="heart failure"){
        subdata=subset(outcomeall, select=c(State,Hospital.Name,Hospital.30.Day.Death..Mortality..Rates.from.Heart.Failure))
        
    }else{
        subdata=subset(outcomeall, select=c(State,Hospital.Name,Hospital.30.Day.Death..Mortality..Rates.from.Pneumonia))
    }
    
    
    ## Return hospital name in that state with lowest 30-day death
    ## get the statistics for each hospital
    test=split(subdata,subdata$State)
    out=lapply(test,function(x){
    stat=tapply(as.numeric(x[,3]),as.factor(x[,2]),mean)
    stat <- stat[!is.na(stat)]
    stat=sort(stat)
    if(num=="best"){num=1}
    else if(num=="worst"){num=length(stat)}
    names(stat[num])})
    out=as.matrix(out)
    state=row.names(out)
    result=cbind(out,state)
    colnames(result)=c('hospital','state')
    result
}
