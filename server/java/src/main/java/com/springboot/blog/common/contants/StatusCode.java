package com.springboot.blog.common.contants;

public enum StatusCode {
    OK(200,"操作成功"),

    UNLOGIN(400, "用户未登录"),
    EXECEPTION(500, "系统异常"),
    ANTI_REPETITION_ERROR(501, "请勿重复请求"),
    SERVER_BUSYNESS(502, "服务器繁忙"),
    NO_ACCESS(600, "无权限操作"),
    NOT_CONDITION(445, "条件未达到");

    private StatusCode(int code, String message){
        this.code = code;
        this.message = message;
    }

    private int code;
    private String message;
    public int getCode() {
        return code;
    }
    public String getMessage() {
        return message;
    }
}
