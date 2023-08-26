import React, { useEffect, useState } from "react";
import "./App.css";
 
function App() {
    const [data, setdata] = useState({
        valorMeuCaninoFeliz: 0,
        valorVaiRex: 0,
        date: 0,
        escolha: 0,
    });

    useEffect(() => {
        fetch("/").then((res) =>
            res.json().then((data) => {
                setdata({
                    valorMeuCaninoFeliz: data.ValorMeuCaninoFeliz,
                    valorVaiRex: data.ValorVaiRex,
                    valorChowChawgas: data.ValorChowChawgas,
                    escolha: data.Escolha,
                });
            })
        );
    }, []);
 
    return (
        <div className="App">
            <header className="App-header">
                <div className="Result">
                  <h2>Total no Meu Canino Feliz: R$ {data.valorMeuCaninoFeliz}</h2>
                  <h2>Total na Vai Rex: R$ {data.valorVaiRex} </h2>
                  <h2>Total no valorChowChawgas: R$ {data.valorChowChawgas}</h2>
                  <h1>{data.escolha} escolhido!!!</h1>
                </div>
            </header>
        </div>
    );
}
 
export default App;