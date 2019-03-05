CREATE TABLE IF NOT EXISTS `user` (
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `account` VARCHAR UNIQUE NOT NULL,
    `password` VARCHAR NOT NULL ,
    `nick_name` VARCHAR(100) NOT NULL COMMENT '昵称',
    `role` SMALLINT NO NULL DEFAULT 1 COMMENT '角色',
    `avatar` VARCHAR COMMENT '头像',
    `github` VARCHAR default '',
    PRIMARY KEY `id`
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户';

CREATE TABLE IF NOT EXISTS `article`(
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `uid` bigint(20) NOT NULL COMMENT '作者',
    `title` VARCHAR(255) NOT NULL COMMENT '文章标题',
    `content` VARCHAR NOT NULL COMMNET '文章内容',
    `like` int(11) NOT NULL DEFAULT 0 COMMENT '点赞数',
    `view` int unsigned NOT NULL DEFAULT 0 COMMENT '浏览数',
    `reply` int unsigned NOT NULL DEFAULT 0 COMMENT '回复数',
    `shared` int unsigned NOT NULL default 0 COMMENT '被分享次数',
    `ctime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `mtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP '更新时间',
    `tag` int(11) NOT NULL COMMENT '文章标签',
    `comment_id` bigint(20) NOT NULL COMMENT '评论'
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='文章';

CREATE TABLE IF NOT EXISTS `tag` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(100) NOT NULL COMMNET '标签名称',
    `ctime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `mtime` timestamp NOT NULL DEFAULT CURREMT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    PRIMARY KEY `id`
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='文章标签';

CREATE TABLE IF NOT EXISTS `role` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL DEFAULT '' COMMENT '角色名',
  `op_user` varchar(20) NOT NULL DEFAULT '' COMMENT '操作人',
  `ctime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `mtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT '角色';


CREATE TABLE IF NOT EXISTS `comment` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `uid` bigint(20)
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT '';

CREATE TABLE IF NOT EXISTS `comment_reply`(

)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT '';

CREATE TABLE IF NOT EXISTS `message_board`(

)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT '';

CREATE TABLE IF NOT EXISTS `message_board_reply`(

)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT '';

