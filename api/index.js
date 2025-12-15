module.exports = (req, res) => {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Content-Type', 'application/json');
    
    res.status(200).json({ 
        status: 'ok', 
        message: 'XyraPanel Backend API',
        endpoints: {
            report: 'POST /api/report'
        }
    });
};
