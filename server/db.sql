CREATE TABLE IF NOT EXISTS `user` (
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `account` VARCHAR(100) UNIQUE NOT NULL,
    `password` VARCHAR NOT NULL ,
    `nick_name` VARCHAR(100) NOT NULL COMMENT '昵称',
    `role` SMALLINT NO NULL DEFAULT 1 COMMENT '角色',
    `avatar` VARCHAR COMMENT '头像',
    `github` VARCHAR COMMENT 'github',
    PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户';

CREATE TABLE IF NOT EXISTS `article`(
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `uid` bigint(20) NOT NULL COMMENT '作者',
    `title` VARCHAR(255) NOT NULL COMMENT '文章标题',
    `content` VARCHAR NOT NULL COMMENT '文章内容',
    `like` int(11) NOT NULL DEFAULT 0 COMMENT '点赞数',
    `terrible` int(11) NOT NULL DEFAULT 0 COMMENT '踩',
    `view` int(11) unsigned NOT NULL DEFAULT 0 COMMENT '浏览数',
    `reply` int(11) unsigned NOT NULL DEFAULT 0 COMMENT '回复数',
    `shared` int(11) unsigned NOT NULL default 0 COMMENT '被分享次数',
    `ctime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `mtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    `tag` int(11) NOT NULL COMMENT '文章标签',
    `comment_id` bigint(20) NOT NULL COMMENT '评论',
    PRIMARY KEY (`id`),
    KEY `ctime_idx` (`ctime`) USING BTREE,
    KEY `view_idx` (`view`) USING  BTREE
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='文章';

CREATE TABLE IF NOT EXISTS `tag` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(100) NOT NULL COMMENT '标签名称',
    `ctime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `mtime` timestamp NOT NULL DEFAULT CURREMT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='文章标签';

CREATE TABLE IF NOT EXISTS `role` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `op_user` bigint(20) NOT NULL COMMENT '操作人',
  `name` varchar(128) NOT NULL DEFAULT '' COMMENT '角色名',
  `ctime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `mtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT '角色';

CREATE TABLE IF NOT EXISTS `comment` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `uid` bigint(20) NOT NULL ,
  `aid` bigint(20) NOT NULL ,
  `ctime` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`),
  KEY `ctime_idx` (`ctime`) USING BTREE
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT '评论';

CREATE TABLE IF NOT EXISTS `comment_reply`(
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `uid` bigint(20) NOT NULL ,
  `cid` bigint(20) NOT NULL ,
  `ctime` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间'
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT '评论回复';

