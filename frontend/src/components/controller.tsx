import {useState} from 'react'


function Controller(){
    const [isLoading, setIsLoading] = useState(false)
    const [message,setMessage] = useState<any[]>([])


    const createBlobUrl = (data: any) => {
        
    }


    const handleStop = async () => {}
  
    return(
      <div className="h-screen overflow-y-hidden">
         <div className="flex flex-col justify-between h-full overflow-y-scroll"></div>
      </div>
    )
}



export default Controller