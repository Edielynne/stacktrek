import React from 'react'

const Posts = ({posts}) => {

    let d = posts.map( (info) =>{
        return  <div className="card">
  
        <div className="container">
        <h4><b>{info.name}</b> </h4>
        <i>{info.supplier}</i>
        <p>{info.description}</p>
        <p>{info.price}</p>
        </div>
  
        </div>
    })
    return (
        <div className="post"> 
            <div className="grid-container">
  <div className="grid-item">{d}</div>        
            
        </div>
           </div>         
        )
    }
export default Posts