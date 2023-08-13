import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './News.css';

const News = () => {
  const [category, setCategory] = useState('politics');
  const [news, setNews] = useState([]);

  useEffect(() => {
    const fetchNews = async () => {
      const apiKey = '5b56c3a81cb448ad98461fa2279f8d51';
      const response = await axios.get(
        `https://newsapi.org/v2/top-headlines?category=${category}&apiKey=${apiKey}`
      );
      setNews(response.data.articles);
    };

    fetchNews();
  }, [category]);

  return (
    <div>
      <h2>News</h2>
      <div>
        <button onClick={() => setCategory('politics')}>Politics</button>
        <button onClick={() => setCategory('sports')}>Sports</button>
        <button onClick={() => setCategory('health')}>Health</button>
      </div>
      <div>
        {news.map((article, index) => (
          <div key={index}>
            <h3>{article.title}</h3>
            <p>{article.description}</p>
            <a href={article.url} target="_blank" rel="noopener noreferrer">
              Read more
            </a>
          </div>
        ))}
      </div>
    </div>
  );
};

export default News;
