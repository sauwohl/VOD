_base_ = [
    '../../../_base_/datasets/nway_kshot/few_shot_voc_ms.py',
    '../../../_base_/schedules/schedule.py', '../../vfa_r101_c4.py',
    '../../../_base_/default_runtime.py'
]
# classes splits are predefined in FewShotVOCDataset
# FewShotVOCDefaultDataset predefine ann_cfg for model reproducibility.
data = dict(
    train=dict(
        save_dataset=True,
        dataset=dict(
            type='FewShotVOCDefaultDataset',
            ann_cfg=[dict(method='MetaRCNN', setting='SPLIT1_2SHOT')],
            num_novel_shots=2,
            num_base_shots=2,
            classes='ALL_CLASSES_SPLIT1',
        )),
    val=dict(classes='ALL_CLASSES_SPLIT1'),
    test=dict(classes='ALL_CLASSES_SPLIT1'),
    model_init=dict(classes='ALL_CLASSES_SPLIT1'))
evaluation = dict(
    interval=800, class_splits=['BASE_CLASSES_SPLIT1', 'NOVEL_CLASSES_SPLIT1'])
checkpoint_config = dict(interval=800)
optimizer = dict(lr=0.001)
lr_config = dict(warmup=None)
runner = dict(max_iters=800)
load_from = 'work_dirs/vfa_r101_c4_8xb4_voc-split1_base-training/iter_9000.pth'

# iter_18000_0718_pascal
# iter_18000_0109_nv10.pth

# model settings
model = dict(frozen_parameters=[
    'backbone', 'shared_head',  'aggregation_layer',  'rpn_head',
])