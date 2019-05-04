create TABLE IF NOT EXISTS `user` (
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `account` VARCHAR(20) UNIQUE NOT NULL COMMENT '账号',
    `role` int(11) NOT NULL COMMENT '角色',
    `permissions` int(11) NOT NULL COMMENT '权限信息',
    `password` VARCHAR(20) NOT NULL COMMENT '密码',
    `nick_name` VARCHAR(100) NOT NULL COMMENT '昵称',
    `avatar` VARCHAR(100) COMMENT '头像',
    `github` VARCHAR(100) COMMENT 'github',
    PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户';

create TABLE IF NOT EXISTS `article`(
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `uid` bigint(20) NOT NULL COMMENT '作者',
    `title` VARCHAR(255) NOT NULL COMMENT '文章标题',
    `content` VARCHAR(1024) NOT NULL COMMENT '文章内容',
    `status` TINYINT(1) NOT NULL COMMENT '0-草稿，1-正文，2-已删除',
    `clap` int(11) NOT NULL DEFAULT 0 COMMENT '鼓掌数',
    `terrible` int(11) NOT NULL DEFAULT 0 COMMENT '踩',
    `visits` int(11) unsigned NOT NULL DEFAULT 0 COMMENT '浏览数',
    `replies` int(11) unsigned NOT NULL DEFAULT 0 COMMENT '回复数',
    `shared` int(11) unsigned NOT NULL default 0 COMMENT '被分享次数',
    `ctime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `mtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON update CURRENT_TIMESTAMP COMMENT '更新时间',
    PRIMARY KEY (`id`),
    KEY `ctime_idx` (`ctime`) USING BTREE,
    KEY `visits_idx` (`visits`) USING  BTREE,
    KEY `clap_idx` (`clap`) USING BTREE,
    KEY `replies_idx` (`replies`) USING BTREE,
    KEY `status_idx` (`status`) USING BTREE
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='文章';

create TABLE IF NOT EXISTS `tag` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(100) NOT NULL COMMENT '标签名称',
    `ctime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `mtime` timestamp NOT NULL DEFAULT CURREnT_TIMESTAMP ON update CURRENT_TIMESTAMP COMMENT '更新时间',
    PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='文章标签';


create TABLE IF NOT EXISTS `article_tag` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `aid` bigint(20) NOT NULL COMMENT '文章id',
    `tid` int(11) NOT NULL COMMENT '标签id',
    PRIMARY KEY (`id`),
    KEY `aid_idx` (`aid`) USING BTREE,
    KEY `tid_idx` (`tid`) USING BTREE
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='文章标签';

create TABLE IF NOT EXISTS `role` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `op_user` bigint(20) NOT NULL COMMENT '操作人',
  `name` varchar(128) NOT NULL DEFAULT '访客' COMMENT '角色名',
  `ctime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `mtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON update CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT '角色';

create TABLE IF NOT EXISTS `comment` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `uid` bigint(20) NOT NULL ,
  `aid` bigint(20) NOT NULL ,
  `content` varchar(512) NOT NULL DEFAULT '' COMMENT '评论内容',
  `ctime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `mtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON update CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `ctime_idx` (`ctime`) USING BTREE
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT '评论';

create TABLE IF NOT EXISTS `comment_reply`(
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `uid` bigint(20) NOT NULL ,
  `cid` bigint(20) NOT NULL ,
  `content` varchar(256) DEFAULT '' COMMENT '回复内容',
  `ctime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT '评论回复';


create TABLE IF NOT EXISTS `privilege` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `op_user` bigint(20) NOT NULL DEFAULT 1 COMMENT '操作人',
  `remark` varchar(20) NOT NULL DEFAULT '' COMMENT '权限备注',
  `ctime` timestamp NOT NULL DEFAULT CURREnT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT '只读权限'
