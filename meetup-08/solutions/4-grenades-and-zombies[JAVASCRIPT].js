function killZombies(board){ // Returns an array

    // VARIABLES
    const dimensions = board.length;
    let zombiesFound = 0;
    let startX = 0;

    // POPULATE GRID WITH ZEROES
    let solutionGrid = Array(dimensions).fill(0).map(x => Array(dimensions).fill(0));
    
    // I like to start from y
    for(let y = 0; y < dimensions; y++){
        // initialize next row
        if(zombiesFound > 0){ // if found more than 0 zombies
            // fill the grid with zombie fatalities
            for(let fill = startX; fill < dimensions; fill++){
                solutionGrid[fill][y-1] += zombiesFound;
            }
            zombiesFound = 0; // reset
        }    
        startX = 0;    
    
    
        for(let x = 0; x < dimensions; x++){
            if(board[x][y] === 1){ // reached a wall            
                if(zombiesFound > 0){ // if found more than 0 zombies                
                    // fill the grid with zombie fatalities
                    for(let fill = startX; fill < x; fill++){
                        solutionGrid[fill][y] += zombiesFound;
                    }
                    zombiesFound = 0; // reset
                }        
                startX = x+1; // set to next square
                continue;
            }
            if(board[x][y] === 2){ // if there is a zombie            
                zombiesFound++; // increase zombie count and fill vertically;
                for(let up = y-1; up > 0; up--){
                    if(board[x][up] === 1) break;
                    solutionGrid[x][up]++;
                }
                for(let down = y + 1; down < dimensions; down++){
                    if(board[x][down] === 1) break;
                    solutionGrid[x][down]++;
                }
            }
        }
    }
    if(zombiesFound > 0){ // if found more than 0 zombies            
        // fill the grid with zombie fatalities
        for(let fill = startX; fill < dimensions; fill++){
            solutionGrid[fill][dimensions-1] += zombiesFound;
        }
        zombiesFound = 0; // reset
    }
    
    let best = 1;
    let bestArray = [];

    for(let x = 0; x < dimensions; x++){
        for(let y = 0; y < dimensions; y++){
            if(solutionGrid[x][y] === best) bestArray.push("[" + x + ", " + y + "]"); 
            else if(solutionGrid[x][y] > best){
                best = solutionGrid[x][y];
                bestArray = [];
                bestArray.push("[" + x + ", " + y + "]"); 
            }
        }
    }
    return bestArray;
}
