const getIp = function(req){
    let ip = req.get("X-Real-IP") || req.get("X-Forwarded-For") || req.ip
    if(ip.split(',').length>0){
        ip = ip.split(',')[0]
    }
    return ip
}

//TODO fix 数据不准确

module.exports = getIp