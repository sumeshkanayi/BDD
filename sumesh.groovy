freeStyleJob('myFree') {
  description("myjob")
  
  
}
freeStyleJob('myFree2') {
  description("myjob2")
  scm{
    git{
      
      remote{
       
        url('https://github.com/sumeshkanayi/BDD.git')
        
      }
      
    }
  }
  
  
}
freeStyleJob('myFree3') {
  description("myjob3")
  
  
}

pipelineJob('test_pipeline'){
  
  definition{
    
    cpsScm{
      
      scm{
        
        git{
          
          remote{
            
           url('https://github.com/sumeshkanayi/myrepo.git') 
          }
        }
        
      }
      
      
    }
    
    
    
  }
  
  
  
  
}
