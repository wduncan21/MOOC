pollutantmean=function(folder,pollutant,id=1:332){
    ## this function takes the folder, the type of polutant and the ids to be included
    ##calculates the mean exluding the NAs
    library(stringr)
    
    readid=str_pad(readid, 3, pad = "0")
    
    masterfolder='B:\\OneDrive\\Documents\\coursera\\R programming\\'
    
    dataset=do.call('rbind',lapply(id,function(x){
        
    file=paste(masterfolder,folder,'\\',x,'.csv',sep='')
    
    read.csv(file)
    }
    )
    )
    targetcolumn=dataset[pollutant]
    
    targetcolumn=targetcolumn[!is.na(targetcolumn)]
    
    mean(targetcolumn)
}


complete=function(folder,id=1:332){
    
    library(stringr)

    readid=str_pad(id, 3, pad = "0")
    
    dataset=do.call('rbind',lapply(readid,function(x){
        
    file=paste(masterfolder,folder,'\\',x,'.csv',sep='')
    
    read.csv(file)
    }
    )
    )
    completesulfate=dataset[!is.na(dataset$sulfate),]
    completeall=completesulfate[!is.na(completesulfate$nitrate),]
    info=as.data.frame(table(completeall$ID))
    colnames(info)=c('id','nobs')
    output=info[match(id,info$id),]
    output
}


corr=function(folder,threshold=0){
    
    library(stringr)
    
    id=1:332
    
    readid=str_pad(id, 3, pad = "0")
    
    dataset=do.call('rbind',lapply(readid,function(x){
        
    file=paste(masterfolder,folder,'\\',x,'.csv',sep='')
    
    read.csv(file)
    }
    )
    )
    completesulfate=dataset[!is.na(dataset$sulfate),]
    completeall=completesulfate[!is.na(completesulfate$nitrate),]
    info=as.data.frame(table(completeall$ID))
    colnames(info)=c('id','nobs')
    obs_num=info[match(id,info$id),]
    
    obs_sub=subset(obs_num,nobs>threshold)    
    
    obs_sub=obs_sub$id
    
    selected_data=completeall[completeall$ID %in% obs_sub,]
    
    cor_table=do.call('c',lapply(obs_sub,function(x){
        
    set_for_corr=selected_data[selected_data$ID == x, ]
    
    cor(set_for_corr$sulfate,set_for_corr$nitrate)
    
    }))
    
}
    
    
    
    
    
    