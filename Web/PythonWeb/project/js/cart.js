$(function (){
    //1.全选和取消全选
    $(".checkAll").click(function(){
        if($(this).attr("checked")){
            //修改为取消选中
            $(this).removeAttr("checked")
                .attr("src","../images/cart/product_normal.png")
            $(".checkItem")
            .attr("src","../images/cart/product_normal.png")
        }else{
            $(this).attr("checked","true")
                .attr("src","../images/cart/product_true.png")
            $(".checkItem")
            .attr("src","../images/cart/product_true.png")
        }
        /* 
        1.为全选按钮增加点击事件，事件函数中，判断当前按钮是否为选中
        状态（查看是否存在checked属性值）
        2.如果当前元素存在checked状态值， */
        sum();
        
    })
    //2.反选
    $(".checkItem").click(function (){
        if ($(this).attr("checked")){
            $(this).removeAttr("checked")
                .attr("src","../images/cart/product_normal.png")
        }else{
            $(this).attr("checked","true")
                .attr("src","../images/cart/product_true.png")
        }
        //被选中的商品数量等于商品元素的个数，视为全选
        //console.log($(".checkItem[checked]"));
        if($(".checkItem[checked").length 
        == $(".checkItem").length){
            //视为全选
            $(".checkAll")
            .attr("src","../images/cart/product_true.png")
        }else{
            $(".checkAll")
            .attr("src","../images/cart/product_normal.png")
        }
        sum();
    })
    //3.数量增减
    $(".add").click(function (){
        //获取前一个兄弟元素（输入框）的值
        var value = $(this).prev().val();
        value++;
        $(this).prev().val(value);
        
        countPrice($(this),value);
        sum();
    })
    $(".minus").click(function (){
        //获取前一个兄弟元素（输入框）的值
        var value = $(this).next().val();
        if (value > 1){
            value--;
        }
        
        $(this).next().val(value);
        countPrice($(this),value);
        sum();

    })
    function countPrice(that,value){
        //价格联动 单价*数量，修改总金额
        var str = that.parents(".item").find(".gprice p")
            .html();
            var price = str.substring(2);
            var sum = price * value;
            sum=sum.toFixed(2);//取两位小数
            that.parent().next().html("￥ "+sum);
    }
    //移除
    $(".item .action").click(function (){
        //移除整个商品记录
        $(this).parents(".item").remove();
        sum();
    })
    //计算商品总数量和总价格
    function sum(){
        //获取选中的商品，累加商品数量和总价
        var sum = 0;//保存总数量
        var price = 0;//保存总价格
        //数据遍历，each(function(){})
        $(".checkItem[checked]").each(function (){
            //每取到一个元素就调用当前函数,this指代函数的调用者
            var n = $(this).parents(".item")
            .find(".gcount input").val();

            var p = $(this).parents(".item")
            .find(".gsum input").val()
            //转Number()
            n = Number(n);
            
            p = Number(p.substring(2));
            sum += n;
            price += p;
            
        });
        $(".total-num").html(sum);
        $(".total-price").html(price);
    }

})

