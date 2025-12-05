import { useEffect, useRef, useState } from 'react';
export default function Captura(){
  const videoRef = useRef(null);
  const [ready,setReady] = useState(false);
  useEffect(()=>{
    async function init(){
      try{
        const s = await navigator.mediaDevices.getUserMedia({video:true});
        videoRef.current.srcObject = s;
        setReady(true);
      }catch(e){
        console.error(e);
      }
    }
    init();
  },[]);
  return (<div style={{fontFamily:'system-ui',padding:20}}>
    <h2>Captura</h2>
    <video ref={videoRef} autoPlay playsInline style={{width:'640px',height:'480px',background:'#000'}}/>
    <p>{ready? 'Câmera ativa' : 'Aguardando permissão...'}</p>
  </div>)
}
