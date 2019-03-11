package com.springboot.blog.common.paramcheck;

import com.springboot.blog.common.contants.StatusCode;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Target(ElementType.FIELD)
@Retention(RetentionPolicy.RUNTIME)
public @interface CheckNotEmpty {
    StatusCode statusCode() default StatusCode.EXECEPTION;
}
