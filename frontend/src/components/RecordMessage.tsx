import { ReactMediaRecorder } from "react-media-recorder"
import RecordIcon from "./RecordIcon"

 type Props = {
    handleStop:any;
 }



const RecordMessage = ({handleStop}:Props) => {


       return (

        <>
        <ReactMediaRecorder
         audio
         onStop={handleStop}
         render={({status,startRecording,stopRecording}) => 
         <div className="mt-2"> <button onMouseDown={startRecording} 
         onMouseUp={stopRecording}
         className="bg-white p-4 rounded-full"> Icon</button></div>}
        
        />
        </>
       )
    

}



export default RecordMessage