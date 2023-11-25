import axios from 'axios';
import { useRef, useState } from 'react';
import './style.scss';

const UploadButton = (props) => {
    const filePicker = useRef(null);

    const handlePick = () => {
        filePicker.current.click();
    };

    const handleChange = async (e) => {
        e.preventDefault();
        let files = [...e.target.files];
        const formData = new FormData();

        switch (files.length) {
            case 1:
            case 3:
                formData.append('file', files);
                const res = await axios.post('127.0.0.1/uploadone', formData);
                const data = await res.json();
                props.setImg(data);
                files.length == 1 ? props.setMessage(files[0].name) : props.setMessage(`${files[0].name} и др.`);
                break;

            default:
                props.setMessage('ОШИБКА! Выберите 1 или 3 файла с расширением .CSV');
                break;
        }
    };

    return (
        <div className='btn'>
            <button
                className='btn_area'
                onClick={handlePick}
            >Загрузить файлы</button>
            <input
                type="file"
                id="input_files"
                name="files"
                ref={filePicker}
                onChange={handleChange}
                accept=".csv"
                multiple
            />
        </div>
    );
};

export default UploadButton;