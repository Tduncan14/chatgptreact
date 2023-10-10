import {useState} from 'react'
import axios from 'axios'


type Props = {
    setMessages:any;

}

function Title({setMessages}:Props){


    const[isResetting,setIsResetting] = useState(false);



    // Reset the conversation

    const resetConversation = async() => {
         setIsResetting(true)

         await axios.get("http://localhost:8000/reset").then((res) =>{

         if(res.status = 200){
              setMessages([])
         }
         else{
            console.error("There is a problem with the api request")
         }
        


         }).catch(err => {
            console.error(err.message)
         })




         setIsResetting(false)
    }

    return(
        <div>
            <button  onClick={resetConversation} className="bg-indigo-100 p-5">Push Me</button>
        </div>
    )
}

export default Title