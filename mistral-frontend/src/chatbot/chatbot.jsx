import React, { useState, useRef, useEffect } from 'react';
import './chatbot.css';
import SendIcon from '@mui/icons-material/Send';
import axios from 'axios';
import Skeleton from '@mui/material/Skeleton';
import TypeWriter from '../TypeWriter/TypeWriter'
import { MistralUrl } from '../Constant';

const Chat = () => {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState('');
    const chatWindowRef = useRef(null);
    const [Loading, setLoading] = useState(false)

    const sendMessage = () => {
        setLoading(true)
        if (input.trim()) {
            let body = {
                user_query: input
            }

            setMessages([...messages, { text: input, user: 'You' }]);

            setInput('');
            axios
                .post(`${MistralUrl}get_response`, body)
                .then((res) => {

                    setMessages((prevMessages) => [
                        ...prevMessages,
                        { text: res.data.response, user: 'Bot' }
                    ]);
                    setLoading(false)
                    console.log(res.data.response)
                })
            // Simulate a bot response
            // setTimeout(() => {
            //     setMessages((prevMessages) => [
            //         ...prevMessages,
            //         { text: `${input}`, user: 'Bot' }
            //     ]);
            // }, 1000);
        }
    };


    const scrollToBottom = () => {
        if (chatWindowRef.current) {
            chatWindowRef.current.scrollTop = chatWindowRef.current.scrollHeight;
        }
    };

    useEffect(() => {
        scrollToBottom();
    }, [messages]);

    const handleKeyPress = (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    };

    return (
        <div className="chat-container">
            <div className="messages" ref={chatWindowRef}>
                {
                    messages.length === 0 ?
                        <img
                            className='mistralLogo'
                            src='Icons\le-chat-logo-light.webp'>
                        </img>
                        :
                        <>

                            {messages.map((msg, index) => (
                                <div key={index} className={`message ${msg.user === 'You' ? 'user' : 'bot'}`}>
                                    <div className="message-content">
                                        {
                                            msg.user === 'You' ?
                                                <>
                                                    <img className='Vhsimage' src='Icons\VHSlogo.png'>
                                                    </img>
                                                    <div style={{ marginTop: 5, fontSize: '1.25rem', color: '#fafaf9' }}>

                                                        {msg.text}
                                                    </div>
                                                </>
                                                :
                                                <>
                                                    <img className='image' src='Icons\announcing-mistral.png'>
                                                    </img>
                                                    <div style={{ marginTop: 7, fontSize: 16, fontWeight: 300, color: '#ccc' }}>
                                                        <p style={{ fontWeight: 300, margin: 0 }}>
                                                            <TypeWriter text={msg.text} />
                                                        </p>
                                                    </div>
                                                </>
                                        }



                                    </div>
                                </div>
                            ))}
                            {
                                Loading ?
                                    <div className="message-content">
                                        <img className='image1' src='Icons\announcing-mistral.png'>
                                        </img>
                                        <div>

                                            <Skeleton sx={{ bgcolor: 'grey.900' }} width={700} animation="wave" />
                                            <Skeleton sx={{ bgcolor: 'grey.900' }} width={700} animation="wave" />
                                            <Skeleton sx={{ bgcolor: 'grey.900' }} width={700} animation="wave" />
                                        </div>
                                    </div>
                                    :
                                    <></>
                            }
                        </>
                }
            </div>
            <div className="input-container">
                <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    onKeyPress={handleKeyPress}
                    placeholder="Ask anything!"
                />
                <SendIcon className='sendIcon' onClick={sendMessage}>Send</SendIcon>
            </div>
            <p className='PoweredBy' >
                Powered By-
                <a
                    style={{ textDecoration: "none" }}
                    href={`https://dev-webapp.precium.ai/`}
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    <span
                        style={{
                            color: "#fd6f00",
                            textDecoration: "none",
                            fontWeight: 600,
                        }}
                    >
                        {"  "}
                        Mistral Ai
                    </span>
                </a>
            </p>
        </div>
    );
};

export default Chat;
