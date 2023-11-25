import { useState } from 'react';
import UploadButton from './components/uploadButton/UploadButton.jsx';
import UploadDragDrop from './components/uploadDragDrop/UpoadDragDrop.jsx';
import graph from './img/growth.png';
import './styles/App.scss';

function App() {
    const [message, setMessage] = useState('Выберите 1 или 3 файла с расширением .CSV');
    const [img, setImg] = useState();

    return (
        <>
            <section className='main-part'>
                <div className='main-left'>
                    <h2 className='tittle-web'>Оценка эффективности вложения в недвижимость</h2>

                    <UploadButton 
                        setMessage={setMessage} 
                        setImg={setImg} 
                    />

                    <UploadDragDrop 
                        message={message} 
                        setMessage={setMessage} 
                        setImg={setImg} 
                    />

                    { message == '_' 
                        ? <p className='message' style={{opacity: '0'}}>{message}</p> 
                        : <p className='message'>{message}</p> 
                    }
                </div>

                <div className='main-right'>
                    <img className='graph' src={graph} />
                    { <img className='graph' src={img} /> }
                </div>
            </section>
        </>
    );
};

export default App;
