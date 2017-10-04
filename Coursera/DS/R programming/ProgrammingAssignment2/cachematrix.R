## These functions calculate the inverse of the matrix and cache it.
## If inverse is already calculated, then we use the cached data instead of calculating again


## This function MakeCacheMatrix creates a special "matrix" that can cache the inverse


makeCacheMatrix <- function(x = matrix()) {
    m <- NULL
    set <- function(y) {
        x <<- y
        m <<- NULL
    }
    get <- function() x
    setinverse <- function(inverse) m <<- inverse
    getinverse <- function() m
    list(set = set, get = get,
         setinverse = setinverse,
         getinverse = getinverse)
}



## This function cacheSolve calculates the inverse if it does not exists, or print the cached inverse 
## if already calculated, the output is to return a matrix that is the inverse of the input
cacheSolve <- function(x, ...) {
    m <- x$getinverse()
    ## check if the inverse is calculated already
    ## if calculated, print the cached data
    if(!is.null(m)) {
        message("getting cached data")
        return(m)
    } 
    ## if not calculated, then calculate the inverse
    else {
        data <- x$get()
        m <- solve(data,...)
        x$setinverse(m)
        m
    }
}
