import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './News.css';

const defaultImages = [
  'https://example.com/default-image-1.jpg',
  'https://example.com/default-image-2.jpg',
  
];

const getRandomDefaultImage = () => {
  const randomIndex = Math.floor(Math.random() * defaultImages.length);
  return defaultImages[randomIndex];
};

const NewsCard = ({ article, isSelected, onClick, onClose }) => {
  return (
    <div className="news-card" onClick={onClick}>
      <img
        className="news-image"
        src={article.urlToImage || getRandomDefaultImage()}
        alt={article.title}
      />
      <h3 className="news-title">{article.title}</h3>
      <p className="news-description">{article.description}</p>

      {isSelected && (
        <div className="news-modal" onClick={onClose}>
          <div className="news-modal-content" onClick={(e) => e.stopPropagation()}>
            <img
              className="news-modal-image"
              src={article.urlToImage || getRandomDefaultImage()}
              alt={article.title}
            />
            <h3 className="news-modal-title">{article.title}</h3>
            <p className="news-modal-description">{article.content}</p>
            <a className="news-modal-link" href={article.url} target="_blank" rel="noopener noreferrer">
              Read more
            </a>
            <button className="news-modal-close" onClick={onClose}>
              Close
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

const News = () => {
  const [category, setCategory] = useState('politics');
  const [news, setNews] = useState([]);
  const [selectedModalIndex, setSelectedModalIndex] = useState(null);

  useEffect(() => {
    const fetchNews = async () => {
      const apiKey = '5b56c3a81cb448ad98461fa2279f8d51'; // Your API key
      try {
        const response = await axios.get(
          `https://newsapi.org/v2/top-headlines?category=${category}&apiKey=${apiKey}`
        );
        setNews(response.data.articles);
      } catch (error) {
        console.error('Error fetching news:', error);
      }
    };

    fetchNews();
  }, [category]);

  return (
    <div className="news-container">
      <h2>News</h2>
      <div className="news-category-buttons">
        <button className="news-category-button" onClick={() => setCategory('politics')}>
          Politics
        </button>
        <button className="news-category-button" onClick={() => setCategory('sports')}>
          Sports
        </button>
        <button className="news-category-button" onClick={() => setCategory('health')}>
          Health
        </button>
      </div>
      <div className="news-cards">
        {news.map((article, index) => (
          <NewsCard
            key={index}
            article={article}
            isSelected={index === selectedModalIndex}
            onClick={() => setSelectedModalIndex(index)}
            onClose={() => setSelectedModalIndex(null)}
          />
        ))}
      </div>
    </div>
  );
};

export default News;
