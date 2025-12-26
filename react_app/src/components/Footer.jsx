import "./Footer.css";

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-container">
        <div className="footer-section">
          <h3>PoetryHub</h3>
          <p>Платформа для поэтов нового поколения</p>
          <p className="footer-copyright">
            © {new Date().getFullYear()} PoetryHubPlatform
          </p>
        </div>
        <div className="footer-sections">
          <h4>Разделы</h4>
          <ul className="footer-links">
            <li>
              <a href="/">Главная</a>
            </li>
            <li>
              <a href="/">Все стихи</a>
            </li>
            <li>
              <a href="/">Авторы</a>
            </li>
            <li>
              <a href="/">Подборки</a>
            </li>
          </ul>
        </div>

        <div className="footer-sections">
          <h4>Контакты</h4>
          <div className="social-links">
            <a href="" className="social-icon" aria-label="Telegram">
              📱
            </a>
            <a href="" className="social-icon" aria-label="GitHub">
              💻
            </a>
            <a href="" className="social-icon" aria-label="Email">
              ✉️
            </a>
          </div>
          <p className="footer-email">contact@poetryhub.ru</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
