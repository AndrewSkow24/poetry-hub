import "./Header.css";

const Header = () => {
  return (
    <header className="header">
      <div className="header-container">
        <div className="logo">
          <h1>PoetryHubPlatform</h1>
          <span className="logo-subtitle">
            Платформа для поэтов нового поколения
          </span>
        </div>

        <nav className="nav">
          <a href="/" className="nav-link active">
            Главная
          </a>
          <a href="/" className="nav-link">
            Стихи
          </a>
          <a href="/" className="nav-link">
            Авторы
          </a>
          <a href="/" className="nav-link">
            О проекте
          </a>
        </nav>

        <div className="user-actions">
          <button className="btn btn-login">Войти</button>
          <button className="btn btn-register">Регистрация</button>
        </div>
      </div>
    </header>
  );
};

export default Header;
