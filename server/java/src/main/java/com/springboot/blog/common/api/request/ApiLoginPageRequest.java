package com.springboot.blog.common.api.request;

import lombok.Data;

@Data
public class ApiLoginPageRequest extends ApiLoginRequest{
    private Integer pageNum;

    private Integer pageSize;
}
