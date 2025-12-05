import Link from 'next/link';
export default function Home(){
  return (<div style={{fontFamily:'system-ui',padding:20}}>
    <h1>Escudo Orofacial - Frontend</h1>
    <p><Link href='/captura'>Ir para captura</Link></p>
  </div>)
}
