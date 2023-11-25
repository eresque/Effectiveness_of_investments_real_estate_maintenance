import axios from 'axios';
import { useState } from 'react';
import './style.scss';

const UploadDragDrop = (props) => {
    const [drag, setDrag] = useState(false);

    const dragStartHandler = (e) => {
        e.preventDefault();
        setDrag(true);
    };

    const dragLeaveHandler = (e) => {
        e.preventDefault();
        setDrag(false);
    };

    const onDropHandler = async (e) => {
        e.preventDefault();
        let files = [...e.dataTransfer.files];

        const formData = new FormData();
        let flag = false;
        files.map(item => {
            if (item.type != 'text/csv') {
                flag = true;
            }
        });

        if (flag) {
            props.setMessage('ОШИБКА! Выберите файлы с расширением .CSV');
            setDrag(false);
            return;
        }

        switch (files.length) {
            case 1:
            case 3:
                formData.append('file', files);
                const res = await axios.post('127.0.0.1/uploadone', formData);
                const data = await res.json();
                props.setImg(data);
                files.length == 1 ? props.setMessage(files[0].name) : props.setMessage(`${files[0].name} и др.`);
                setDrag(false);
                break;

            default:
                props.setMessage('ОШИБКА! Выберите 1 или 3 файла с расширением .CSV');
                setDrag(false);
                break;
        }
    };

    return (
        <div className='drag_drop'>
            {drag
                ? <div
                    className='drop_area active'
                    onDragStart={e => dragStartHandler(e)}
                    onDragEnd={e => dragLeaveHandler(e)}
                    onDragOver={e => dragStartHandler(e)}
                    onDrop={e => onDropHandler(e)}
                >Отпустите файлы</div>
                : <div
                    className='drop_area sleep'
                    onDragStart={e => dragStartHandler(e)}
                    onDragEnd={e => dragLeaveHandler(e)}
                    onDragOver={e => dragStartHandler(e)}
                >Перетащите файлы в область</div>
            }
        </div>
    );
};

export default UploadDragDrop;