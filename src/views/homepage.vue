<template>
  <div v-show="mainDlg == 'main'">
    <div class="ai-header flex items-center">
      <div class="relative">
        <img class="header-img" :src="getImage('icon_mu')" @click="showmenu = !showmenu" />
        <div v-show="showmenu" class="absolute bg-white left-12 z-10">
          <ul class="menu_ul">
            <li class="font_menu flex items-center justify-start w-44 m-2 p-2 pl-4" @click="typeSelectDlg=true;showmenu=false;"><img :src="getImage('icon_menu_1')" /><div class="ml-2">新建项目</div></li>
            <li class="font_menu flex items-center justify-start w-44 m-2 p-2 pl-4"><img :src="getImage('icon_menu_2')" /><div class="ml-2">项目列表</div></li>
            <li class="font_menu flex items-center justify-start w-44 m-2 p-2 pl-4"><img :src="getImage('icon_menu_3')" /><div class="ml-2">保存项目</div></li>
            <li class="font_menu flex items-center justify-start w-44 m-2 p-2 pl-4"><img :src="getImage('icon_menu_4')" /><div class="ml-2">打开文件</div></li>
            <li class="font_menu flex items-center justify-start w-44 m-2 p-2 pl-4"><img :src="getImage('icon_menu_5')" /><div class="ml-2">下载文件</div></li>
            <li class="font_menu flex items-center justify-start w-44 m-2 p-2 pl-4"><img :src="getImage('icon_menu_6')" /><div class="ml-2">社区</div></li>
            <li class="font_menu flex items-center justify-start w-44 m-2 p-2 pl-4"><img :src="getImage('icon_menu_7')" /><div class="ml-2">帮助中心</div></li>
            <li class="font_menu flex items-center justify-start w-44 m-2 p-2 pl-4"><img :src="getImage('icon_menu_8')" /><div class="ml-2">个人中心</div></li>
            <li class="font_menu flex items-center justify-start w-44 m-2 p-2 pl-4"><img :src="getImage('icon_menu_9')" /><div class="ml-2">反馈</div></li>
          </ul>
        </div>
      </div>
      <div class="header-title cursor-pointer" v-if="typeSelectDlg" @click="showmenu = !showmenu">Playable ML Module</div>
      <div style="width:668px;margin-left:442px" v-else>
        <el-steps :space="200" :active="currentStep">
          <el-step title="创建数据集" />
          <el-step title="创建模型" />
          <el-step title="训练" />
          <el-step title="结果" />
        </el-steps>
      </div>
    </div>
    <div class="flex justify-center items-center flex-col" style="margin-top:107px" v-if="typeSelectDlg">
      <div class="font_tip_title" style="margin-left: -1370px;">开始一个新的项目</div>
      <div class="flex justify-center items-center">
        <div class="type-box">
          <div>
            <img class="type-image" :src="getImage('home-card1')" />
          </div>
          <div>
            <p class="type-title">图像分类</p>
            <p class="type-p">分类识别是监督式机器学习最常见的使用场景。</p>
            <p class="type-p" style="color:rgba(153, 153, 153, 0.8);font-size:14px;top: 391px;top:465px">20000人已学习</p>
            <div class="type-btn" @click="typeSelectDlg = false;currentStep=0">
              <span>开始学习</span>
            </div>
          </div>
        </div>
        <div class="type-box">
          <div>
            <img class="type-image" :src="getImage('home-card2')" />
          </div>
          <div>
            <p class="type-title">机器翻译</p>
            <p class="type-p">机器翻译是人工智能的终极目标之一，其核心语言理解和语言生成是自然语言处理的两大基本问题。</p>
            <p class="type-p" style="color:rgba(153, 153, 153, 0.8);font-size:14px;top: 391px;top:465px">15000人已学习</p>
            <div class="type-btn">
              <span>开始学习</span>
            </div>
          </div>
        </div>
        <div class="type-box">
          <div>
            <img class="type-image" :src="getImage('home-card3')" />
          </div>
          <div>
            <p class="type-title">预测分析</p>
            <p class="type-p">预测分析包括各种统计技术，用于分析当前和历史事实，对未来做出预测。</p>
            <p class="type-p" style="color:rgba(153, 153, 153, 0.8);font-size:14px;top: 391px;top:465px">5000人已学习</p>
            <div class="type-btn">
              <span>开始学习</span>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <div class="flex justify-center items-center flex-col" style="margin-top:107px" v-show="currentStep == 0">
        <div class="font_tip_title" style="margin-left: -1170px;">创建数据集</div>
        <div class="" style="margin-left: -940px;">你可以直接选择下面的数据集也可以创建你自己的数据集</div>
        <div class="flex justify-center items-center">
          <div class="data-box">
            <div class="flex justify-center items-center border-b-2" style="height:220px">
              <img class="data-image" :src="getImage('data_dog')" />
            </div>
            <div>
              <p class="data-title">猫狗识别</p>
              <p class="data-p">该数据集包含猫狗照片各5000张。</p>
              <div class="data-btn">
                <div class="gray-btn" @click="mainDlg = 'doc'"><span>查看</span></div>
                <div class="blue-btn" @click="currentStep = 1"><span>使用</span></div>
              </div>
            </div>
          </div>
          <div class="data-box">
            <div class="flex justify-center items-center border-b-2" style="height:220px">
              <img class="data-image" :src="getImage('data_number')" />
            </div>
            <div>
              <p class="data-title">手写数字识别</p>
              <p class="data-p">该数据集包含10000张书写数字。</p>
              <div class="data-btn">
                <div class="gray-btn"><span>查看</span></div>
                <div class="blue-btn"><span>使用</span></div>
              </div>
            </div>
          </div>
          <div class="data-box">
            <div class="flex flex-col justify-center items-center h-full data-add">
              <div class="w-24 h-24 flex justify-center items-center" style="background:rgba(72, 68, 163, 0.1);">
                <img class="data-image" :src="getImage('data_add')" />
              </div>
              <div>创建你自己的分类数据集</div>
            </div>
          </div>
        </div>
      </div>
      <div v-show="currentStep == 1" style="margin: 0px 0 0 150px;">
        <div class="flex mt-8">
          <div class="model-font cursor-pointer w-32 h-12 flex justify-center items-center" style="background: #F2F2F2;" :class="{cur:model_type == 'model'}" @click="model_type='model'"><span>模型库</span></div>
          <div class="model-font cursor-pointer w-32 h-12 flex justify-center items-center" style="background: #F2F2F2;" :class="{cur:model_type == 'editor'}" @click="model_type='editor'"><span>自定义</span></div>
        </div>
        <div class="font_tip_title flex my-6" v-show="model_type == 'model'">
          以下机器学习模型为经典的分类模型，你可以尝试不同的模型，运行并查看效果
        </div>
        <div class="font_tip_title flex my-6" v-show="model_type == 'editor'">
          你可以自定义编辑更多分类模型，运行并查看效果
        </div>
        <div v-show="model_type == 'model'">
          <div class="model-list flex justify-center items-center">
            <div class="model-img flex justify-center items-center"><img :src="getImage('img_model1')" /></div>
            <div class="model-title">
              <p class="title">Convolutional neural networks (CNN)卷积神经网络</p>
              <ul class="type flex">
                <li>图像识别</li>
                <li>效果好，性能高</li>
              </ul>
              <p class="des">卷积神经网络（CNN）是一类强大的、为处理图像数据而设计的神经网络。</p>
              <p class="num">2000人已使用</p>
            </div>
            <div class="blue-btn cursor-pointer" @click="currentStep = 2;modelTarinType='cnn'"><span>使用</span></div>
            <div class="model-arrow cursor-pointer" @click="modelScript2 = false;modelScript1 = !modelScript1">
              <img v-show="!modelScript1" :src="getImage('model-arrow')" />
              <img v-show="modelScript1" :src="getImage('model-arrow-up')" />
            </div>
          </div>
          <div class="model-script" v-if="modelScript1">
            <div class="script-title">认识CNN</div>
            <div class="script-p">
              <p>卷积神经网络 (CNN)是一种用于处理图像的神经网络,这种类型的神经网络从图像中获取输入并从图像中提取特征,并提供可学习的参数以有效地进行分类、检测和更多任务。我们使用称为“过滤器”的东西从图像中提取特征,我们使用不同的过滤器从图像中提取不同的特征。</p>
              <p>CNN 的关键在于认识到即使有数百万个与输入图像的像素相关的参数，也不一定有数百万个不同的参数。CNN 由所谓的过滤器的集合或“库”组成，这些过滤器是比原始图像小得多的矩形图像块。这些过滤器在对应于卷积数学运算的过程中与图像上的不同位置匹配，因此得名 CNN。</p>
            </div>
            <div class="script-title">卷积神经网络的原理</div>
            <div class="script-p">
              <p>让我们试一试：猫的耳朵</p>
              <p>这是一个简单的小部件，您可以在其中通过将过滤器参数设置为 -1、0 或 +1 来调整它们。该小部件将自动将过滤器应用于左侧的猫图像。生成的激活值显示在右侧面板中。</p>
              <p>继续尝试更改过滤器参数。从底部的选择器中选择一个值，然后单击中间面板过滤器中的像素。您可能首先会在输出面板中复制 cat 模式——如果您选择值 -1，则否定。当过滤器同时包含负值和正值时，更有趣的事情开始发生，因此同时包含 -1 和 +1。</p>
              <p>这不是一个实际的练习，而是尝试调整过滤器，以便检测图像中的耳朵，或者换句话说，以便在输出图像中在猫的耳朵周围获得白点。</p>
            </div>
            <div class="script-img flex justify-center"><img :src="getImage('img_cnn')"/></div>
            <div class="script-title">关于CNN更多学习入口</div>
            <div class="script-link"><a>Crash Course in Convolutional Neural Networks for Machine Learning</a></div>
            <div class="script-link"><a>Rash Course in Convolutional Neural Networks for Machine Learning</a></div>
            <div class="script-title">模型公式</div>
            <div class="script-p">你可以修改编辑模型；点击立即使用，可运行查看训练效果</div>
            <div class=" block">
              <mathEditor :isShowTitle="false" :isShowFoot="true" modelType="cnn" @changeActivation="changeActivation" @changeCurrentStep="changeCurrentStep"></mathEditor>
            </div>
          </div>
          <div class="model-list flex justify-center items-center">
            <div class="model-img flex justify-center items-center"><img :src="getImage('img_model2')" /></div>
            <div class="model-title">
              <p class="title">Multi-Layer Perception (MLP)多层感知器</p>
              <ul class="type flex">
                <li>图像识别</li>
                <li>语音识别</li>
                <li>机器翻译</li>
              </ul>
              <p class="des">MLP多层感知器是一种前向结构的ANN人工神经网络, 它能够处理非线性可分离的问题，值得深入研究。MLP算法应用范围较广，扩展性也强，可应用于语音识别、图像识别、机器翻译等领域。</p>
              <p class="num">1000人已使用</p>
            </div>
            <div class="blue-btn cursor-pointer" @click="currentStep = 2;modelTarinType='mlp'"><span>使用</span></div>
            <div class="model-arrow cursor-pointer" @click="modelScript1 = false;modelScript2 = !modelScript2">
              <img v-show="!modelScript2" :src="getImage('model-arrow')" />
              <img v-show="modelScript2" :src="getImage('model-arrow-up')" />
            </div>
          </div>
          <div class="model-script" v-if="modelScript2">
            <div class="script-title">认识MLP</div>
            <div class="script-p">
              <p>MLP由三层组成——输入层、隐藏层和输出层。输入层仅接收输入，隐藏层处理输入，输出层生成结果。基本上，每一层都要训练权值。</p>
              <p>使用MLP用于：Tabular data 列表数据，Image data 图像数据，Text data 文本数据。</p>
            </div>
            <div class="script-title">多层感知器的优势</div>
            <div class="script-p">多层感知器能够学习任意非线性函数。因此，这些网络被普遍称为通用函数逼近器。通用逼近背后的主要原因之一是激活函数(activation
              function)。激活函数将非线性特征引入网络中，有助于网络学习输入和输出之间的复杂关系。</div>
            <div class="script-img flex justify-center"><img :src="getImage('img_mlp')"/></div>
            <div class="script-title">关于MLP更多学习入口</div>
            <div class="script-link"><a>Crash Course in Convolutional Neural Networks for Machine Learning</a></div>
            <div class="script-link"><a>Rash Course in Convolutional Neural Networks for Machine Learning</a></div>
            <div class="script-title">模型公式</div>
            <div class="script-p">你可以修改编辑模型；点击立即使用，可运行查看训练效果</div>
            <div class=" block">
              <mathEditor :isShowTitle="false" :isShowFoot="true" modelType="mlp" @changeActivation="changeActivation" @changeCurrentStep="changeCurrentStep"></mathEditor>
            </div>
          </div>
          <div class="model-list flex justify-center items-center">
            <div class="model-img flex justify-center items-center"><img :src="getImage('img_model3')" /></div>
            <div class="model-title">
              <p class="title">K-nearest neighbors (KNN) K最临近</p>
              <ul class="type flex">
                <li>分类</li>
                <li>回归</li>
              </ul>
              <p class="des">K 最近邻（KNN）是一种非常简单、易于理解、用途广泛且最顶级的机器学习算法之一。KNN 用于金融、医疗保健、政治学、手写检测、图像识别和视频识别等各种应用。</p>
              <p class="num">500人已使用</p>
            </div>
            <div class="blue-btn"><span>使用</span></div>
            <div class="model-arrow"><img :src="getImage('model-arrow')" /></div>
          </div>
        </div>
        <div v-show="model_type == 'editor'">
          <mathEditor :isShowTitle="false" :isShowFoot="true" @changeCurrentStep="changeCurrentStep"></mathEditor>
        </div>
      </div>
      <div class="flex justify-center" v-show="currentStep == 2 || currentStep == 3" style="margin:32px 100px">
        <div class="w-80 bottom-2 rounded mr-3 p-7 bg-white">
          <div class="font_help_title">训练</div>
          <div class="font_help_title border-2 rounded-lg flex justify-center items-center h-14 my-4 cursor-pointer bg-trainBtn hover:bg-trainBtnHover"
               :class="{train_btn:trainState}" @click="handleTrain()">
            <div v-if="trainState"><a-spin :indicator="indicator" />训练中</div>
            <div v-else>训练模型</div>
          </div>
          <div class="demo-progress" v-show="trainState || trainEnd">
            <el-progress :percentage="percentage"/>
          </div>
          <div class="font_help_title my-4">
            超参数调节
          </div>
          <div class="border-b">
            <div class="font_help_p inline-block">Epochs</div>
            <el-tooltip
              class="box-item"
              effect="dark"
              placement="top"
            >
              <template #content> 
                <div style="width:400px">
                  Epoch<br />
                  一个epoch意味着训练数据集中的每个样本都至少通过一次训练模型，例如如果您的epoch设置为50，这意味着您的模型被训练50次。通常，数字越大，您的模型将更好地学习预测模型。<br />
                  你可能想要调整（通常是增加）这个数字，知道您的模型获得良好的预测结果。<br />
                </div>
              </template>
              <img class="inline-block ml-1 mb-1 cursor-pointer" :src="getImage('icon_help')" />
            </el-tooltip>
            <div class="my-4">
              <el-input-number style="width:90px" v-model="epochsValue" :min="1" :max="100" controls-position="right"/>
            </div>
          </div>
          <div class="border-b">
            <div class="font_help_p inline-block mt-2">Learning Rate</div>
            <el-tooltip
              class="box-item"
              effect="dark"
              placement="top"
            >
              <template #content>
                <div style="width:400px">
                  Optimizer<br />
                  优化器就是在深度学习反向传播过程中，指引损失函数（目标函数）的各个参数往正确的方向更新合适的大小，使得更新后的各个参数让损失函数（目标函数）值不断逼近全局最小。<br />
                  你可能想要更换不同优化器使您的模型获得良好的预测结果。<br />
                </div>
              </template>
              <img class="inline-block ml-1 mb-1 cursor-pointer" :src="getImage('icon_help')" />
            </el-tooltip>
            <div class="my-4">
              <el-input-number style="width:90px" v-model="rateValue" :step="0.01" :min="0" :max="1" controls-position="right"/>
            </div>
          </div>
          <div class="border-b">
            <div class="font_help_p inline-block mt-2">Batch Size</div>
            <el-tooltip
              class="box-item"
              effect="dark"
              placement="top"
            >
              <template #content>
                <div style="width:400px">
                  Batch size<br />
                  批次是在一次训练迭代中使用的一组样本。例如，假设您有80张图像，而且您选择16 batch size，这意味着数据将被分为80/16=5个批次。一旦所有5个批次都通过模型输入，恰好完成一个epoch。<br />
                  您可能不需要调整这个数字来获得良好的训练结果。<br />
                </div>
              </template>
              <img class="inline-block ml-1 mb-1 cursor-pointer" :src="getImage('icon_help')" />
            </el-tooltip>
            <div>
              <a-radio-group v-model:value="batchValue">
                <a-radio :style="radioStyle" :value="16">16</a-radio>
                <a-radio :style="radioStyle" :value="32">32</a-radio>
                <a-radio :style="radioStyle" :value="64">64</a-radio>
                <a-radio :style="radioStyle" :value="128">128</a-radio>
              </a-radio-group>
            </div>
          </div>
          <div class="">
            <div class="font_help_p inline-block mt-2">Optimizer</div>
            <el-tooltip
              class="box-item"
              effect="dark"
              placement="top"
            >
              <template #content>
                <div style="width:400px">
                  Optimizer<br />
                  优化器就是在深度学习反向传播过程中，指引损失函数（目标函数）的各个参数往正确的方向更新合适的大小，使得更新后的各个参数让损失函数（目标函数）值不断逼近全局最小。<br />
                  你可能想要更换不同优化器使您的模型获得良好的预测结果。<br />
                </div>
              </template>
              <img class="inline-block ml-1 mb-1 cursor-pointer" :src="getImage('icon_help')" />
            </el-tooltip>
            <div>
              <a-radio-group v-model:value="optimizerValue">
                <a-radio :style="radioStyle" value="Adam">Adam</a-radio>
                <a-radio :style="radioStyle" value="RMSprop">RMSprop</a-radio>
                <a-radio :style="radioStyle" value="SGD">SGD</a-radio>
                <a-radio :style="radioStyle" value="Adamax">Adamax</a-radio>
                <a-radio :style="radioStyle" value="Adagrad">Adagrad</a-radio>
              </a-radio-group>
            </div>
          </div>
        </div>
        <div class="bottom-2 rounded p-7 bg-white" style="width:1164px">
          <div class="font_help_title">可视化面板</div>
          <div class="relative w-full flex items-center rounded" style="height: 97px;">
            <div class="title-font flex items-center rounded" style="background: #F2F2F2;">
              <span class="px-5 py-2 cursor-pointer" :class="{help_cur: showDLgType == 1}" @click="showDLgType = 1">折线图</span>
              <span class="px-5 py-2 cursor-pointer" :class="{help_cur: showDLgType == 2}" @click="showDLgType = 2">图像可视化</span>
              <span class="px-5 py-2 cursor-pointer" :class="{help_cur: showDLgType == 3}" @click="showDLgType = 3">训练日志</span>
            </div>
            <div class="cursor-pointer ml-4"><img :src="getImage('icon_plus_box')" /></div>
          </div>
          <div class="flex h-3/4">
            <div class="flex items-center flex-col h-full w-full mt-32" v-show="!trainEnd && showDLgType == 1">
              <img :src="getImage('img_train')" />
              <div class="font_tarin">点击训练模型，查看更多数据</div>
            </div>
            <div class="iframebox" v-show="trainEnd && showDLgType == 1">
              <div class="box"><a target="_blank" :href="curpreviewurl">点击进入详情</a></div>
              <iframe id="myiframe" width="100%" height="100%" :src="curpreviewurl"></iframe>
            </div>
            <div v-if="showDLgType == 3" style="width: 100%">
              <el-table :data="tableData" style="width: 100%">
                <el-table-column fixed="left" prop="ai_id" label="训练ID" width="150" />
                <el-table-column prop="ai_model" label="AI Module" width="120" />
                <el-table-column prop="ai_activation" label="Activation" width="120" />
                <el-table-column prop="ai_epochs" label="Epochs" width="120" />
                <el-table-column prop="ai_rate" label="Learning rate" width="120" />
                <el-table-column prop="ai_batch" label="Batch size" width="120" />
                <el-table-column prop="ai_optimizer" label="Optimizer" width="120" />
                <el-table-column prop="ai_loss" label="Train/loss" width="160" />
                <el-table-column prop="ai_acc" label="Train/acc" width="160" />
                <el-table-column prop="ai_tarintime" label="Time" width="150" />
                <el-table-column prop="ai_time" label="Submission time" width="150" />
                <el-table-column fixed="right" label="Operations" width="120">
                  <template #default>
                    <el-button link type="primary" size="small">导出</el-button>
                    <el-button link type="primary" size="small">运行</el-button>
                  </template>
                </el-table-column>
              </el-table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-show="mainDlg == 'doc'" style="height: 100vh;">
    <div class="ai-header flex items-center" style="height: 104px;">
      <div class="gray-btn cursor-pointer header-img" @click="mainDlg = 'main'"><span>返回</span></div>
      <!-- <img class="header-img" :src="getImage('icon_back')" @click="mainDlg = 'main'" /> -->
      <div style="width:668px;margin-left:442px">
        <el-steps :space="200" :active="currentStep">
          <el-step title="创建数据集" />
          <el-step title="创建模型" />
          <el-step title="训练" />
          <el-step title="结果" />
        </el-steps>
      </div>
      <div class="blue-btn cursor-pointer" style="position: absolute;right: 50px;" @click="mainDlg = 'main';currentStep = 1"><span>使用</span></div>
    </div>
    <div class="flex justify-center items-center" style="margin-top:32px">
      <div class="doc_side">
        <div class="doc_data flex items-center relative">
          <div class="absolute left-6" style="">数据集</div>
          <img class="absolute right-2 cursor-pointer" :src="getImage('icon_add_file')" />
        </div>
        <ul class="doc_type">
          <li class="flex items-center relative h-12 cursor-pointer" :class="{cur:doc_type == 'cat'}" @click="doc_type = 'cat'">
            <p class="absolute left-10" style="color: #121212;">猫类数据集</p>
            <p class="absolute right-2" style="color: #979797;">500</p>
          </li>
          <li class="flex items-center relative h-12 cursor-pointer" :class="{cur:doc_type == 'dog'}" @click="doc_type = 'dog'">
            <p class="absolute left-10" style="color: #121212;">狗类数据集</p>
            <p class="absolute right-2" style="color: #979797;">500</p>
          </li>
        </ul>
      </div>
      <div class="doc_main px-14 py-7">
        <div class="doc_upload h-12 flex items-center">
          <el-upload
            v-model:file-list="fileList"
            class="upload-demo"
            action=""
            multiple
          >
            <img class="mx-4 my-3 cursor-pointer" :src="getImage('icon_upload')" />
          </el-upload>
          <!-- <img class="mx-4 my-3 cursor-pointer" :src="getImage('icon_upload')" /> -->
        </div>
        <div class="doc_imgs flex items-center flex-wrap">
          <div class="relative" v-for="item in 20">
            <img class="mx-4 my-3 w-40 h-36" :src="getImageDataset(String(item))" />
            <img class="absolute top-5 right-6" :src="getImage('icon_delete')" />
            <div class="absolute bottom-5 left-6 px-2 text-center rounded" style="background: #FF3B5C;color: #ffffff;">{{doc_type}}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import axios from 'axios'
import { LoadingOutlined } from '@ant-design/icons-vue';
import { ref, onMounted, reactive, watch, h } from "vue";
import { useRouter, useRoute } from "vue-router";
import { ElMessage } from 'element-plus'
import mathEditor from "./matheditor.vue"
const router = useRouter()
const route = useRoute()
const currentStep = ref(0);
let typeSelectDlg = ref(true)
let mainDlg = ref('main')
let checked = ref(true)
let doc_type = ref('cat')
let model_type = ref('model')
let modelScript1 = ref(false)
let modelScript2 = ref(false)
let showmenu = ref(false)
const getImage = (name: string): string => {
  return new URL(`../assets/images/home/${name}.png`, import.meta.url).href;
};
// const getImageDataset = (name: string): string => {
//   return new URL(`../assets/images/home/${doc_type.value}/${name}.jpg`, import.meta.url).href;
// };
const getImageDataset = (name: string): string => {
  return new URL(`../../back/data/cats_and_dogs_filtered/train/${doc_type.value}s/${doc_type.value}.${name}.jpg`, import.meta.url).href;
};

const jumpTo = (route:string) => {
  router.push({name: route})
}
onMounted(() => {
  console.log(route)
  document.querySelector('body')!.style.backgroundColor = '#F6F6F6'
  if(route.params.currentStep){
    typeSelectDlg.value = false
    currentStep.value = Number(route.params.currentStep)
  }
})
const indicator = h(LoadingOutlined, {
  style: {
    fontSize: '24px',
    marginRight: '12px',
    color: '#ffffff'
  },
  spin: true,
});
let trainState = ref(false)
let trainEnd = ref(false)
let curpreviewurl = ref('http://127.0.0.1:6008/#scalars')
let percentage = ref(0)
let fileList:any = []
let timeInterval:any = null
let tablekey = 1
let modelTarinType = ref('cnn')
let modelTarinActivation = ref('Relu')
const changeActivation = (value:string) => {
  modelTarinActivation.value = value
}
const changeCurrentStep = (value:number) => {
  currentStep.value = value
}
let tableData:any = ref([])
const handleTrain = async () => {
  if(trainState.value == true) {
    ElMessage('上次训练还未完成，请稍后重试')
    return
  }
  percentage.value = 0
  if(timeInterval){clearInterval(timeInterval)}
  curpreviewurl.value = ''
  trainState.value = true
  trainEnd.value = false
  let startTime:any = new Date()
  const step = Number(Number(50/Number(epochsValue.value)/22).toFixed(2))
  console.log(currentStep)
  timeInterval = setInterval(() => {
    let temp = Number((percentage.value+step).toFixed(2))
    percentage.value = temp
    if (percentage.value > 100) {
      percentage.value = 100
    }
  }, 500)
  let res = await axios({
    method: 'post',
    url: '/update/tensorflow',
    data: {
      epochsValue: epochsValue.value,
      rateValue: rateValue.value,
      batchValue: batchValue.value,
      optimizerValue: optimizerValue.value,
    }
  });
  let endTime:any = new Date()
  if(res.data.msg_code == 200) {
    let item = {
      key: tablekey,
      ai_id: '猫狗识别_log/run' + tablekey,
      ai_model: modelTarinType.value,
      ai_activation: modelTarinActivation.value,
      ai_epochs: epochsValue.value,
      ai_rate: rateValue.value,
      ai_batch: batchValue.value,
      ai_optimizer: optimizerValue.value,
      ai_loss: res.data.data.loss,
      ai_acc: res.data.data.accuracy,
      ai_tarintime: setBackLogTime(endTime-startTime),
      ai_time: formatDateTime(endTime,'yyyy-MM-dd hh:mm')
    }
    tableData.value.push(item)
    tablekey++
    setTimeout(() => {
      curpreviewurl.value = 'http://127.0.0.1:6008/#scalars'
      trainState.value = false
      trainEnd.value = true
      currentStep.value = 3
      percentage.value = 100
    }, 2000);
  }
}
const radioStyle = reactive({
  display: 'block',
  height: '30px',
  lineHeight: '30px',
});

let showDLgType = ref(1)
let epochsValue = ref(15)
let rateValue = ref(0.01)
let batchValue = ref(16)
let optimizerValue = ref('RMSprop')
const setDateTimePrefix = (dateTime: number): string => {
    return dateTime < 10 ? `0${dateTime}` : `${dateTime}`;
}
const setBackLogTime = (mss: any) => {
    // if (!us) return '00:00:00';
    // // 微秒 转为  毫秒
    // const mss = Math.floor(us / 1000);
    if (!mss) return '00:00:00';
    const days = Math.floor(mss / (1000 * 60 * 60 * 24));
    const hours = Math.floor((mss % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((mss % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((mss % (1000 * 60)) / 1000);
    const res = setDateTimePrefix(hours) + ':' + setDateTimePrefix(minutes) + ':' + setDateTimePrefix(seconds);
    return days ? days + 'day ' + res : res;
}
const formatDateTime = function (date:any, fmt = 'yyyy-MM-dd hh:mm:ss') {
    var o:any = {
        'M+': date.getMonth() + 1, // 月份
        'd+': date.getDate(), // 日
        'h+': date.getHours(), // 小时
        'm+': date.getMinutes(), // 分
        's+': date.getSeconds(), // 秒
        'S': date.getMilliseconds() // 毫秒
    };
    if (/(y+)/.test(fmt)) {
        fmt = fmt.replace(RegExp.$1, (date.getFullYear() + '').substr(4 - RegExp.$1.length));
    }
    for (var k in o) {
        if (new RegExp('(' + k + ')').test(fmt)) {
            let str = o[k] + '';
            fmt = fmt.replace(RegExp.$1, (RegExp.$1.length === 1) ? str : ('00' + str).substr(str.length));
        }
    }
    return fmt;
};
</script>
<style scoped>
p {
  margin: 0;
}

.header-img {
  margin-left: 50px;
  cursor: pointer;
}

.header-title {
  margin-left: 10px;
  font-family: 'PingFang SC';
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 56px;
  color: #4844A3;
}

.data-add {
  font-family: 'PingFang SC';
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 28px;
}

.data-add img {
  cursor: pointer;
}

.data-add div {
  margin-top: 20px;
}

.doc_side {
  background-color: #ffffff;
  border-radius: 8px;
  margin-right: 24px;
  width: 244px;
  height: 800px;
  box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.08);
}

.doc_main {
  background-color: #ffffff;
  border-radius: 8px;
  width: 1164px;
  height: 800px;
}

.doc_data {
  font-family: 'PingFang SC';
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  line-height: 24px;
  color: #333333;
  height: 48px;
}

.doc_type {
  font-family: 'PingFang SC';
  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 22px;
  color: #121212;
}

.doc_type .cur {
  background: #EDECF6;
}

.doc_type .cur p:first-child {
  color: #4844A3!important;
}
.font-p{
  font-family: 'PingFang SC';
  font-style: normal;
  font-weight: 500;
  font-size: 24px;
  color: #4844A3;
}
.font_help_title{
  font-family: 'PingFang SC';
  font-style: normal;
  font-weight: 400;
  font-size: 24px;
  line-height: 34px;
  display: flex;
  align-items: center;
  color: #4844A3;
}
.font_tarin{
  font-family: 'PingFang SC';
  font-style: normal;
  font-weight: 400;
  font-size: 24px;
  line-height: 24px;
  color: rgba(0, 0, 0, 0.7);
}
.font_tip_title{
  font-family: 'PingFang SC';
  font-style: normal;
  font-weight: 400;
  font-size: 24px;
  line-height: 34px;
  color: #000000;
}
.font_help_p{
  font-family: 'PingFang SC';
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 22px;
}
.font_menu{
  font-family: 'PingFang SC';
  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 22px;
  color: rgba(0, 0, 0, 0.6);
}
.help_cur{background-color: #ffffff;border: 1px solid #4844A3;border-radius: 4px;}
.train_btn{background-color: #4844A3; color: #ffffff}
.menu_ul li:hover{background-color:rgba(72, 68, 163, 0.1); color: #4844A3;}
.model-font{
  font-family: 'PingFang SC';
  font-style: normal;
  font-weight: 400;
  font-size: 29.179px;
  line-height: 32px;
}
.model-font.cur{background: #FFFFFF;border: 1.45895px solid #4844A3;color: #4844A3;border-radius: 5px;}
.iframebox{width: 100%;height: 100%}
.iframebox .box{width: 59%;height: 59%;z-index: 10;display: flex;justify-content: center;align-items: center;position: absolute;font-size: 20px;color: #5d20c0;}
.iframebox .box a:hover{color: #5d20c0;}
.iframebox .box a{color: #5d20c0;display: none;}
.iframebox .box:hover{background-color: rgba(68, 67, 78, 0.5);}
.iframebox .box:hover a{display: block;}
.demo-progress .el-progress--line {
  width: 290px;
}
</style>