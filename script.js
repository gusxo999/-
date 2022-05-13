
function getLoginPage(){
        document.getElementById("login").innerHTML="<label>아이디</label><input type=\"text\"><label>비밀번호</label><input type=\"password\"><button onclick=\"getStatusPage()\">로그인</button>";
}

function getStatusPage(){
    document.getElementById("login").innerHTML="<form><fieldset><legend>체크리스트</legend><ul><li><label>나이 :</label><input type=\"number\" id=\"age\" ><label>살</label></li><li><label>키 :</label><input type=\"number\" id=\"height\"><label>cm</label></li><li><label>몸무게 :</label><input type=\"number\" id=\"weight\"></li><li><label>근육량 모르면 0 입력 :</label><input type=\"number\" id=\"muscle\"></li><li><label>성별 : </label><input type=\"radio\" id=\"sex\" value=\"남\"  name=\"sex\"><label>남</label><input type=\"radio\" id=\"sex\" value=\"여\" name=\"sex\"><label>여</label></li></ul><button type=\"submit\" onclick=\"getCheckPage()\">확인</button></fieldset></form>";
}
function getCheckPage(){
    const age=document.getElementById("age").value;
    const height=document.getElementById("height").value;
    const weight=document.getElementById("weight").value;
    const muscle=document.getElementById("muscle").value;    
    const sex=document.getElementById("sex").value;
    document.getElementById("login").innerHTML="<table border=\"1\"><tr><td>나이 </td><td id=\"age2\" value=\""+age+"\">"+age+"</td></tr><tr><td>키 </td><td id=\"height2\" value=\""+height+"\">"+height+"</td></tr><tr><td>몸무게</td><td id=\"weight2\" value=\""+weight+"\">"+weight+"</td></tr><tr><td>근육량</td><td id=\"muscle2\" value=\""+muscle+"\">"+muscle+"</td></tr><tr><td>성별</td><td id=\"sex2\" value=\""+sex+"\">"+sex+"</td></tr></table><li>입력한 정보가 맞으십니까?<ul><button onclick=\"getResultPage()\">확인</button></ul><ul><button onclick=\"getStatusPage()\">취소</button></ul></li>"
}
function getResultPage(){
    const age=document.getElementById("age2").innerText;
    const height=document.getElementById("height2").innerText;
    const weight=document.getElementById("weight2").innerText;
    const muscle=document.getElementById("muscle2").innerText;  
    const sex=document.getElementById("sex2").innerText;
    
    
    
    
    if(sex=='남자'){
        const BMC = 66.47 + (13.75 * weight) + (5 * height) - (6.76 * age)
    }
    else{
        BMC = 665.1 + (9.56 * weight) + (1.85 * height) - (4.68 * age)
    }

    const protein = weight * 2 // 섭취 단백질 g
    const my_protein = protein * 4 // 단백질 칼로리
    const BMC_1 = BMC - my_protein // 단백질 제외 칼로리
    const carb = BMC_1 * 0.7
    const my_carb = carb / 4 // 탄수화물 kcal
    const fat = BMC_1 * 0.3 // 지방g
    const my_fat = fat / 9 // 지방kcal


    document.getElementById("login").innerHTML="<table border=\"1\"><tr><td>기초 대사량</td><td id=\"sumkcal\">"+BMC+"</td></tr><tr><td>필요 단백질</td><td id=\"protein\">"+my_protein+"</td></tr><tr><td>필요 탄수화물</td><td id=\"carbon\">"+my_carb+"</td></tr><tr><td>필요 지방</td><td id=\"fat\">"+my_fat+"</td></tr></table></body>"
}