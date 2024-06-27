import React, { useState, useEffect } from 'react'

const TypeWriter = ({ text }) => {
    const [displayText, setDisplayText] = useState('');
    const [currentIndex, setCurrentIndex] = useState(0);

    useEffect(() => {

        console.log(text.length,'currentIndex')

        if (currentIndex < text.length) {
          const timeout = setTimeout(() => {
            setDisplayText((prevText) => prevText + text[currentIndex]);
            setCurrentIndex((prevIndex) => prevIndex + 1);
          },3); // Adjust the timeout duration for typing speed
          return () => clearTimeout(timeout);
        }
      }, [currentIndex, text]);

    return (
        <div>{displayText}</div>
    )
}


export default TypeWriter