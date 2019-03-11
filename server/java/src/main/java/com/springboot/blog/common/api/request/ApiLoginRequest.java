package com.springboot.blog.common.api.request;

import com.springboot.blog.common.api.ApiRequest;
import lombok.Data;

@Data
public class ApiLoginRequest implements ApiRequest {
    /**
     * 用户id
     */
    private String userGuid;

    /**
     * 登录标识
     */
    private String token;
}
