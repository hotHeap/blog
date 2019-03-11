package com.springboot.blog.common.api;

import com.springboot.blog.common.contants.StatusCode;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;

@Data
@Builder
@AllArgsConstructor
@ApiModel(value = "响应结果")
public class ApiResponse<T> {
    /** 响应状态码 */
    @ApiModelProperty("响应状态码")
    private int code;

    @ApiModelProperty("操作成功失败标识")
    private boolean success;

    /** 返回消息 */
    @ApiModelProperty("错误消息")
    private String message;

    /** 发送时间 */
    @ApiModelProperty("发送时间")
    private long sendTime;

    /** 响应数据 */
    @ApiModelProperty("响应数据")
    private T data;

    public ApiResponse() {
        this.success = true;
        this.message = StatusCode.OK.getMessage();
        this.code = success ? StatusCode.OK.getCode() : StatusCode.EXECEPTION.getCode();
        this.sendTime = System.currentTimeMillis();
    }

    public ApiResponse(T t) throws Exception {
        this(true, StatusCode.OK.getMessage(), t);
    }

    public void setData(T data) throws Exception{
        this.success = true;
        this.message = StatusCode.OK.getMessage();
        this.data = data;
        this.code = 200;
        this.sendTime = System.currentTimeMillis();
    }

    public void setError(int code, String message){
        this.success = false;
        this.message = message;
        this.code = code;
    }

    public void setError(StatusCode statusCode){
        this.success = false;
        this.message = statusCode.getMessage();
        this.code = statusCode.getCode();
    }

    /**
     * @throws Exception
     *
     */
    public ApiResponse(boolean success, String message, T data) throws Exception {
        super();
        this.success = success;
        this.message = StatusCode.OK.getMessage();
        this.data = data;
        this.code = success ? StatusCode.OK.getCode() : StatusCode.EXECEPTION.getCode();
    }

    /**
     * @throws Exception
     *
     */
    public ApiResponse(boolean success, String message) throws Exception {
        this(success, message, null);
    }

    public ApiResponse(boolean success, T t) throws Exception {
        this(success, success ? StatusCode.OK.getMessage() : StatusCode.EXECEPTION.getMessage(), t);
    }

    /**
     * @throws Exception
     *
     */
    public ApiResponse(boolean success) throws Exception {
        this(success, success ? StatusCode.OK.getMessage() : StatusCode.EXECEPTION.getMessage(), null);
    }
}
