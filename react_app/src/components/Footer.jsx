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
      </div>
    </footer>
  );
};

export default Footer;
