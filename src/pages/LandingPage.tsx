import React, { useState } from 'react';
import './landing.css';
import lvideo from '../assets/lvideo.mp4';
import avatar1 from '../assets/avatar1.jpeg'; // Example avatar images
import avatar2 from '../assets/avatar2.jpg';
import avatar3 from '../assets/avatar3.jpg';
import avatar4 from '../assets/avatar4.jpg';
import avatar5 from '../assets/avatar5.jpg';
import googleplay from '../assets/googleplay.png';
import appstore from '../assets/appstore.png';

const LandingPage = () => {
    const [isNavOpen, setIsNavOpen] = useState(false);

    const trendingItems = [
        { name: "lonerider", likes: 130, avatar: avatar1 },
        { name: "🐧Estiwar Jaimes DJ🤍", likes: 34, avatar: avatar2 },
        { name: "Krishu bansal", likes: 127, avatar: avatar3 },
        { name: "devasena", likes: 127, avatar: avatar4 },
        { name: "neethu", likes: 127, avatar: avatar5 },
    ];

    // Duplicate the items to create a continuous scroll effect
    const allItems = [...trendingItems, ...trendingItems, ...trendingItems];

    return (
        <div className="landing">
            <header className="header">
                <div className="container">
                    <nav className="nav">
                        <div className="logo">
                            <h3>Kismat</h3>
                        </div>
                        <div className="nav-links-container px-3 space-x-3">
                            <ul className={`nav-links ${isNavOpen ? 'open' : ''}`}>
                                <li><a href="#">Livestreams</a></li>
                                <li><a href="#">Leaderboard</a></li>
                                <li><a href="#">Games</a></li>
                            </ul>
                            <div className="nav-button d-sm-none">
                                <a href="#" className="btn">Download App</a>
                            </div>
                            <div className="nav-toggle" onClick={() => setIsNavOpen(!isNavOpen)}>
                                <div className="hamburger"></div>
                                <div className="hamburger"></div>
                                <div className="hamburger"></div>
                            </div>
                        </div>
                    </nav>
                </div>
            </header>

            <section className="hero">
                <video src={lvideo} autoPlay muted loop className="video-background" />
                <div className="container">
                    <div className="hero-content">
                        <h1>Join the global live-streaming platform</h1>
                        <p>for content creation, social communication, and live entertainment.</p>
                        <div className="auth-buttons">
                            <button className="btn apple-btn"><img src={appstore} alt="App Store" /></button>
                            <button className="btn google-btn"><img src={googleplay} alt="Google Play" /></button>
                        </div>
                    </div>
                </div>
                <section className="trending">
                    <div className="container px-0">
                        <h2 className="px-0">Trending Now</h2>
                        <div className="trending-items px-3">
                            {allItems.map((item, index) => (
                                <div className="trending-item" key={index}>
                                    <div className="avatar" style={{ backgroundImage: `url(${item.avatar})` }}>
                                        <div className="live-badge">LIVE</div>
                                    </div>
                                    <div className="trending-info">
                                        <div className="likes">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-eye" viewBox="0 0 16 16">
                                                <path d="M16 8s-3-5.5-8-5.5S0 8 0 8s3 5.5 8 5.5S16 8 16 8zM8 3c4.418 0 7.523 4 7.523 4S12.418 11 8 11 0.477 7 0.477 7 3.582 3 8 3z" />
                                                <path d="M8 5a3 3 0 1 0 0 6 3 3 0 0 0 0-6zm0 1a2 2 0 1 1 0 4 2 2 0 0 1 0-4z" />
                                            </svg>
                                            <span>{item.likes}</span>
                                        </div>
                                        <h3>{item.name}</h3>
                                    </div>
                                </div>
                            ))}
                        </div>
                    </div>
                    <div className="trendingMask">
                        <div className="circle1"></div>
                        <div className="circle2"></div>
                    </div>
                </section>
            </section>

            <footer className="footer">
                <div className="container">
                    <p>&copy; 2024 Kismat. All rights reserved.</p>
                </div>
            </footer>
        </div>
    );
};

export default LandingPage;
