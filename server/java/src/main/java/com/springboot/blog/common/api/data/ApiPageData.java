package com.springboot.blog.common.api.data;

import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(callSuper=false)
public class ApiPageData extends ApiLoginData{
    private int pageNum;

    private int pageSize;

    private int pages;

    private long totalCount;

    private int isLastPage;
}
