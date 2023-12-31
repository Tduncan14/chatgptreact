import {useState} from 'react'
import Title from './Title'
import RecordMessage from './RecordMessage'


function Controller(){
    const [isLoading, setIsLoading] = useState(false)
    const [message,setMessage] = useState<any[]>([])


    const createBlobUrl = (data: any) => {
        
    }


    const handleStop = async () => {}
  
    return(
      <div className="h-screen overflow-y-hidden">
        <Title setMessages={setMessage}/>
         <div className="flex flex-col justify-between h-full overflow-y-scroll pb-96">
            {/* Recorder */}
       
            <div className="fixed bottom-0 w-full py-6 border-t text-center bg-gradient-to-r from-sky-500 to-green-600">
                <div className="flex justify-center items-center w-full">
                <RecordMessage handleStop= {handleStop}  />
                </div>
            </div>
         </div>
      </div>
    )
}



export default Controller